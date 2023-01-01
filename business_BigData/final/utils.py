import os
import shutil
import time
import logging
import numpy


def pieCharFormatter(pct: float, value: float) -> str:
    absolute = int(numpy.round(pct/100.*numpy.sum(value)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def manageFolder(name: str):
    if not os.path.exists(f'./{name}'):
        os.mkdir(f'./{name}')
    else:
        shutil.rmtree(f'./{name}')  # 等效於 rm -rf ./name
        os.mkdir(f'./{name}')


def getClassName(obj) -> str:
    return f"{type(obj)}"


def get_logger(name):
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        '[%(levelname)s %(asctime)s] %(message)s',
        datefmt='%Y%m%d %H:%M:%S'
    )

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    return logger


# 如果最外層有定義參數，呼叫時必須顯式傳遞
def Logger(objName=''):
    def decorator(func):
        def wrap(*args, **kwargs):
            # reference -> https://stackoverflow.com/questions/35325042/python-logging-disable-logging-from-imported-modules
            logging.getLogger('matplotlib').setLevel(logging.INFO)

            startMsg, endMsg = '', ''
            if objName != '':
                startMsg = f'method {objName}.{func.__name__}() start'
                endMsg = f'method {objName}.{func.__name__}() end'
            else:
                startMsg = f'function {func.__name__}() start'
                endMsg = f'function {func.__name__}() end'

            logger = get_logger('logging')

            logger.info(startMsg)
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time()
            logger.info(endMsg)
            logger.info(f'cost {t2-t1} s')

            return result
        return wrap
    return decorator
