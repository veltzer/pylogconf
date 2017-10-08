import os
import os.path
import logging.config
import logging
import sys

# noinspection PyPackageRequirements
import yaml
import logging_tree
from pyfakeuse.pyfakeuse import fake_use


# noinspection PyPackageRequirements,PyUnresolvedReferences
def setup_scrapy():
    """ This is not needed as we pass 'LOG_ENABLED':False to scrapy at init time """

    def replace_configure_logging(install_root_handler=False, settings=None):
        fake_use(install_root_handler)
        fake_use(settings)

    def replace_log_scrapy_info(settings=None):
        fake_use(settings)

    # scrapy stuff
    import scrapy.utils.log  # for configure_logging
    import scrapy.crawler  # configure_logging, log_scrapy_info
    logging_settings = {
        'LOG_ENABLED': False,
        'LOG_LEVEL': logging.WARN,
    }
    scrapy.utils.log.configure_logging(install_root_handler=False, settings=logging_settings)
    # are you watching closely?!?
    scrapy.crawler.configure_logging = replace_configure_logging
    scrapy.crawler.log_scrapy_info = replace_log_scrapy_info
    # print(scrapy.utils.log.log_scrapy_info)


_print_traceback = None
_drill = None


def _excepthook(p_type, p_value, p_traceback):
    logger = logging.getLogger(__name__)
    # we do not do anything with the traceback
    if _print_traceback:
        print(p_traceback)
    # this loop will drill to the core of the problem
    # use only if this is what you want to show...
    if _drill:
        while p_value.__cause__:
            p_value = p_value.__cause__
    logger.error("Exception occurred, type [%s], value [%s]" % p_type, p_value)


def setup_exceptions():
    """ Only print the heart of the exception and not the stack trace """
    # first set up the variables needed by the _excepthook function
    global _print_traceback, _drill
    _print_traceback = os.getenv("PYLOGCONF_PRINT_TRACEBACK", False)
    _drill = os.getenv("PYLOGCONF_DONT_DRILL", True)
    # now that everything is ready attach the hook
    sys.excepthook = _excepthook


def setup():
    """ setup the logging system """
    default_path_yaml = os.path.expanduser('~/.pylogconf.yaml')
    default_path_conf = os.path.expanduser('~/.pylogconf.conf')
    default_level = logging.INFO

    dbg = os.getenv("PYLOGCONF_DEBUG", False)

    """ try YAML config file first """
    value = os.getenv('PYLOGCONF_YAML', None)
    if value is None:
        path = default_path_yaml
    else:
        path = value
    if os.path.isfile(path):
        _debug('found logging configuration file [{0}]...'.format(path), dbg)
        with open(path) as f:
            config = yaml.load(f.read())
            logging.config.dictConfig(config)
            return

    """ Now try regular config file """
    value = os.getenv('PYLOGCONF_CONF', None)
    if value is None:
        path = default_path_conf
    else:
        path = value
    if os.path.isfile(path):
        _debug('found logging configuration file [{0}]...'.format(path), dbg)
        logging.config.fileConfig(path)
        return

    _debug('logging with level [{0}]...'.format(default_level), dbg)
    logging.basicConfig(level=default_level)
    setup_exceptions()


def show_tree():
    """ Show the logging tree """
    logging_tree.printout()


def _debug(msg, dbg):
    if dbg:
        print(msg)
