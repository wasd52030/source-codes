from enum import Enum
import datetime
import time
import logging


class AzureSpeechConfig(Enum):
    subscription_key = 'f9422c78597d4136910992d17656abf6'.encode('utf-8')
    region = 'eastus'.encode('utf-8')


class AzureTranslateConfig(Enum):
    subscription_key = 'fc614d86c7ea4e84b7cd4d5e6c15c46c'.encode('utf-8')
    region = 'eastus'.encode('utf-8')
    endpoint = "https://api.cognitive.microsofttranslator.com".encode('utf-8')


def Logger(func):
    def wrap(*args, **kwargs):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[%(levelname)s %(asctime)s] %(message)s',
            datefmt='%Y%m%d %H:%M:%S'
        )

        logStream = logging.StreamHandler()
        logStream.setLevel(logging.DEBUG)
        logStream.setFormatter(formatter)

        logFile = logging.FileHandler(
            datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
        )
        logFile.setLevel(logging.DEBUG)
        logFile.setFormatter(formatter)

        logger.addHandler(logStream)
        logger.addHandler(logFile)

        logging.info(f'function {func.__name__}() start')
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        logging.info(f'function {func.__name__}() end')
        logging.info(f'cost {t2-t1} s')

        logger.removeHandler(logStream)
        logger.removeHandler(logFile)

        return result
    return wrap
