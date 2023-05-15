import numpy
import pandas

from sklearn.linear_model import LogisticRegression

from dataPreProcess import dataPreProcess
from utils import manageFolder, Logger, get_logger, Accuracy


@Logger("")
def logisticRegression(
    train_x: numpy.ndarray,
    train_y: numpy.ndarray,
    test_x: numpy.ndarray,
    test_y: numpy.ndarray,
    name: str = "",
):
    global accuracies, featureNames

    # 建立logistic regression模型
    model = LogisticRegression(C=100, random_state=1, solver="lbfgs", multi_class="ovr")

    # 訓練模型
    model.fit(train_x, train_y)

    accuracies.append(
        Accuracy(
            model, model.score(train_x, train_y), model.score(test_x, test_y), name
        )
    )


@Logger("")
def main():
    global accuracies, data, train_x1, test_x1, train_x2, test_x2, train_y, test_y

    # 去空值
    data = dataPreProcess.removeNullByRow(data)

    # Label Encode
    data = dataPreProcess.labelEncoding(data)

    # 切訓練與測試資料
    x1 = data.iloc[:, :-1].values
    x2 = data[
        ["PageValues", "ExitRates", "ProductRelated_Duration"]
    ].values
    y = data.iloc[:, data.shape[1] - 1].values
    train_x1, test_x1, train_y, test_y = dataPreProcess.splitTrainTest(
        # 對x進行標準化
        feature=pandas.DataFrame(dataPreProcess.standardized(x1)),
        label=y,
        test_percent=0.2,
        stratify=y,
    )
    train_y = numpy.ravel(train_y)

    train_x2, test_x2, train_y, test_y = dataPreProcess.splitTrainTest(
        # 對x進行標準化
        feature=pandas.DataFrame(dataPreProcess.standardized(x2)),
        label=y,
        test_percent=0.2,
        stratify=y,
    )
    train_y = numpy.ravel(train_y)

    logisticRegression(train_x1, train_y, test_x1, test_y, "all frature")
    logisticRegression(train_x2, train_y, test_x2, test_y, "picked feature")

    with open(
        "./tables_and_reports/modelAccuracies.txt", encoding="utf-8", mode="w"
    ) as file:
        for accuracy in accuracies:
            print("------------------------------", file=file)
            print(accuracy, file=file)
            print("------------------------------", file=file)
            print(file=file)


if __name__ == "__main__":
    accuracies = []

    manageFolder("tables_and_reports")

    data = pandas.DataFrame()
    data = pandas.read_csv("./online_shoppers_intention.csv")

    # feature names
    featureNames = [*data.columns[1:]]

    train_x1, train_y, test_x1, test_y = (
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
    )

    train_x2, test_x2 = (
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
    )

    logger = get_logger("logging")

    main()
