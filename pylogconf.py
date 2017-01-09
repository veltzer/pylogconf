import os # for getenv
import os.path # for isfile
import logging.config # for dictConfig
import logging # for basicConfig
import yaml # for safe_load
import sys # for exit
import logging_tree # for printout


default_path='logging.yaml'
default_level=logging.INFO
env_key='LOG_CFG'
printout=False
quiet=True

def setup_scrapy():
    """ This is not needed as we pass 'LOG_ENABLED':False to scrapy at init time """
    def replace_configure_logging(install_root_handler=False, settings=None):
        pass
    def replace_log_scrapy_info(settings=None):
        pass
    # scrapy stuff
    import scrapy.utils.log # for configure_logging
    import scrapy.crawler # configure_logging, log_scrapy_info
    settings={
            'LOG_ENABLED': False,
            'LOG_LEVEL': logging.WARN,
    }
    scrapy.utils.log.configure_logging(install_root_handler=False, settings=settings)
    # are you watching closely?!?
    scrapy.crawler.configure_logging=replace_configure_logging
    scrapy.crawler.log_scrapy_info=replace_log_scrapy_info
    #print(scrapy.utils.log.log_scrapy_info)

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
        print('didnt find [{0}], logging with level [{0}]...'.format(path, default_level))
        logging.basicConfig(level=default_level)
    if printout:
        logging_tree.printout()
        sys.exit(0)

def debug():
    """ Show the logging tree """
    logging_tree.printout()
