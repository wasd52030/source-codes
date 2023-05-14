import os
import shutil
import time
import logging
from typing import Callable


class Accuracy:
    def __init__(self, model: object, train: float, test: float) -> None:
        self.model = model
        self.modelName = str(self.model.__class__)[1:-2].split(".")[-1]

        self.train = train
        self.test = test

    def __str__(self) -> str:
        return f"{self.modelName}\n\n訓練集: {self.train}\n測試集: {self.train}"


def manageFolder(name: str):
    if not os.path.exists(f"./{name}"):
        os.mkdir(f"./{name}")
    else:
        shutil.rmtree(f"./{name}")  # 等效於 rm -rf ./name
        os.mkdir(f"./{name}")


def getClassName(obj) -> str:
    return f"{type(obj)}"


def get_logger(name: str = "") -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        "[%(levelname)s %(asctime)s] %(message)s", datefmt="%Y%m%d %H:%M:%S"
    )

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    return logger


# 如果最外層有定義參數，呼叫時必須顯式傳遞
def Logger(objName="") -> Callable:
    def decorator(func) -> Callable:
        def wrap(*args, **kwargs):
            # reference -> https://stackoverflow.com/questions/35325042/python-logging-disable-logging-from-imported-modules
            logging.getLogger("matplotlib").setLevel(logging.INFO)

            startMsg, endMsg = "", ""
            if objName != "":
                startMsg = f"method {objName}.{func.__name__}() start"
                endMsg = f"method {objName}.{func.__name__}() end"
            else:
                startMsg = f"function {func.__name__}() start"
                endMsg = f"function {func.__name__}() end"

            logger = get_logger("logging")

            logger.info(startMsg)
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time()
            logger.info(endMsg)
            logger.info(f"cost {t2-t1} s")

            return result

        return wrap

    return decorator
