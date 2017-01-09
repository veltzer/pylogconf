import os
import os.path
import logging.config
import logging
import yaml
import sys
import logging_tree
from pyfakeuse.pyfakeuse import fake_use

default_path = 'logging.yaml'
default_level = logging.INFO
env_key = 'LOG_CFG'
printout = False
quiet = True


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


def setup():
    """ setup the logging system """
    value = os.getenv(env_key, None)
    if value:
        path = value
    else:
        path = default_path
    if os.path.isfile(path):
        if not quiet:
            print('found logging configuration file [{0}]...'.format(path))
        with open(path) as f:
            config = yaml.load(f.read())
            logging.config.dictConfig(config)
    else:
        print('did not find [{0}], logging with level [{0}]...'.format(path, default_level))
        logging.basicConfig(level=default_level)
    if printout:
        logging_tree.printout()
        sys.exit(0)


def debug():
    """ Show the logging tree """
    logging_tree.printout()
