import os
import time
import logging
from typing import Callable, List


class modelInfo:
    def __init__(self, model: object, modelName: str = "") -> None:
        self.model = model
        self.modelName = (
            str(self.model.__class__)[1:-2].split(".")[-1]
            if modelName == ""
            else modelName
        )

    def __str__(self) -> str:
        res = f"{self.modelName}\n\n"
        for attribute, value in self.__dict__.items():
            if attribute != "model" and attribute != "modelName":
                res += f"{attribute}: {value}\n"
        return res[:-1]


class CrossValidation(modelInfo):
    def __init__(
        self,
        model: object,
        scores: List,
        std: float,
        mean: float,
        modelName: str = "",
    ) -> None:
        super().__init__(model, modelName)

        self.scores = scores
        self.std = std
        self.mean = mean


class modelPerformanceMetrics(modelInfo):
    def __init__(
        self,
        model: object,
        confusionMatrix: List,
        accuracy: float,
        precision: float,
        recall: float,
        f1: float,
        auc:float,
        modelName: str = "",
    ) -> None:
        super().__init__(model, modelName)
        self.confusionMatrix = confusionMatrix
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall
        self.f1 = f1
        self.auc = auc


def resultOutput(path: str, results: List):
    with open(path, encoding="utf-8", mode="w") as file:
        for resut in results:
            print("------------------------------", file=file)
            print(resut, file=file)
            print("------------------------------", file=file)
            print(file=file)


def manageFolder(name: str):
    if not os.path.exists(f"./{name}"):
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
                startMsg = f"function {objName}_{func.__name__}() start"
                endMsg = f"function {objName}_{func.__name__}() end"
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
