import configparser
import logging


logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read('/opt/settings/atfapp.conf')

LOGGING_FILENAME = config['LOGGING']['FILENAME']
LOGGING_LEVEL = config['LOGGING']['LEVEL']
LOGGING_MODE = config['LOGGING']['MODE']
LOGGING_MAXBYTES = config['LOGGING']['MAXBYTES']
LOGGING_BACKUPCOUNT = config['LOGGING']['BACKUPCOUNT']
LOGGING_DELAY = config['LOGGING']['DELAY']

POSTGRES_DB_HOST = config['POSTGRES_DB']['POSTGRES_HOST']
POSTGRES_DB_PORT = config['POSTGRES_DB']['POSTGRES_PORT']
POSTGRES_DB_USERNAME = config['POSTGRES_DB']['POSTGRES_USERNAME']
POSTGRES_DB_PASSWORD = config['POSTGRES_DB']['POSTGRES_PASSWORD']
POSTGRES_DB_NAME = config['POSTGRES_DB']['POSTFRES_DB_NAME']
POSTGRES_DB_DRIVER = config['POSTGRES_DB']['POSTGRES_DRIVER']
CACHE_MAX_EXPIRY_TIME = config['POSTGRES_DB']['CACHE_MAX_EXPIRY_TIME']
