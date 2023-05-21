import numpy
import pandas
from matplotlib import pyplot
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from dataPreProcess import dataPreProcess
from utils import manageFolder, Logger, get_logger, Accuracy


@Logger("")
def randomForestFeatureRank(
    train_x: numpy.ndarray,
    train_y: numpy.ndarray,
    test_x: numpy.ndarray,
    test_y: numpy.ndarray,
):
    global accuracies, featureNames

    # 建立random forest模型
    model = RandomForestClassifier(
        criterion="gini", n_estimators=500, random_state=1, n_jobs=2
    )

    # 訓練模型
    model.fit(train_x, train_y)

    rank = model.feature_importances_
    inidices = numpy.argsort(rank)[::-1]

    with open(
        "./tables_and_reports/featureRank.txt", encoding="utf-8", mode="w"
    ) as file:
        for f in range(train_x.shape[1]):
            print(
                f"%2d) %-*s %f"
                % (f + 1, 30, featureNames[inidices[f]], rank[inidices[f]]),
                file=file,
            )

    featureNames = [featureNames[inidices[f]] for f in range(train_x.shape[1])]
    pyplot.title("Feature Importance")
    pyplot.bar(range(train_x.shape[1]), rank[inidices], align="center")
    pyplot.xticks(range(train_x.shape[1]), featureNames, rotation=90)
    pyplot.xlim([-1, train_x.shape[1]])
    pyplot.tight_layout()
    pyplot.savefig("./plots/featureRank.png")
    logger.info(f"featureRank.png ok！")

    return featureNames


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
    global data, train_x1, train_y, test_x2, test_y

    # 去空值
    data = dataPreProcess.removeNullByRow(data)

    # Label Encode
    data = dataPreProcess.labelEncoding(data)

    # 全部特徵
    x1 = data.iloc[:, :-1].values
    y = data.iloc[:, data.shape[1] - 1].values
    train_x1, test_x1, train_y, test_y = dataPreProcess.splitTrainTest(
        # 對x進行標準化
        feature=pandas.DataFrame(dataPreProcess.standardized(x1)),
        label=y,
        test_percent=0.2,
        stratify=y,
    )
    train_y = numpy.ravel(train_y)

    # 特徵關聯排名
    rank = randomForestFeatureRank(train_x1, train_y, test_x2, test_y)

    # 挑過的特徵
    x2 = data[rank[:3]].values
    train_x2, test_x2, train_y, test_y = dataPreProcess.splitTrainTest(
        # 對x進行標準化
        feature=pandas.DataFrame(dataPreProcess.standardized(x2)),
        label=y,
        test_percent=0.2,
        stratify=y,
    )
    train_y = numpy.ravel(train_y)

    #
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

    manageFolder("plots")
    manageFolder("tables_and_reports")

    data = pandas.DataFrame()
    data = pandas.read_csv("./online_shoppers_intention.csv")

    # feature names
    featureNames = [*data.columns[:-1]]

    train_x1, train_y, test_x2, test_y = (
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
    )

    logger = get_logger("logging")

    main()
