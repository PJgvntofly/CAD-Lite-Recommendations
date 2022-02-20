from asyncio import format_helpers
import logging
import logging.config

def configure_logger(name):
    logging.config.dictConfig({
        'version': 1,
        'formatters':{
            'default': {'format': '%(asctime)s %(levelname)s - %(message)s', 'datefmt': '%m/%d/%Y %H:%M:%S'}
        },
        'handlers': {
            'console': {
                'level': 'CRITICAL',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext//sys.stdout'
            },
            'rec_file': {
                'level': 'DEBUG',
                'formatter': 'default',
                'class': 'logging.handlers.RotatingFileHandler',
                'mode': 'a',
                'filename': './logs/rec_log.log',
                'maxBytes': 10*1024*1024,
                'backupCount': 5,
                'delay': False
            },
            'connection_file': {
                'level': 'DEBUG',
                'formatter': 'default',
                'class': 'logging.handlers.RotatingFileHandler',
                'mode': 'a',
                'filename': './logs/connection_log.log',
                'maxBytes': 1024*1024,
                'backupCount': 5,
                'delay': False
            }
        },
        'loggers':{
            'rec_log': {
                'level': 'INFO',
                'handlers': ['console', 'rec_file']
            },
            'connection_log':{
                'level': 'INFO',
                'handlers': ['console', 'connection_file']
            }
        },
        'disable_existing_loggers': False
    })
    return logging.getLogger(name)

rec_log = configure_logger('rec_log')
connection_log = configure_logger('connection_log')
