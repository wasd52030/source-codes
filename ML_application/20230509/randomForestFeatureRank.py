import numpy
import pandas
from matplotlib import pyplot
from sklearn.ensemble import RandomForestClassifier

from dataPreProcess import dataPreProcess
from utils import manageFolder, Logger, get_logger


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

    for f in range(train_x.shape[1]):
        print(
            f"%2d) %-*s %f" % (f + 1, 30, featureNames[inidices[f]], rank[inidices[f]])
        )

    pyplot.title("Feature Importance")
    pyplot.bar(range(train_x.shape[1]), rank[inidices], align="center")
    pyplot.xticks(range(train_x.shape[1]), featureNames, rotation=90)
    pyplot.xlim([-1, train_x.shape[1]])
    pyplot.tight_layout()
    pyplot.savefig("./plots/featureRank.png")
    logger.info(f"featureRank.png ok！")


@Logger("")
def main():
    global data, train_x, train_y, test_x, test_y

    # 去空值
    data = dataPreProcess.removeNullByRow(data)

    # Label Encode
    data = dataPreProcess.labelEncoding(data)

    # 切訓練與測試資料
    x = data.iloc[:, :-1].values
    y = data.iloc[:, data.shape[1] - 1].values
    train_x, test_x, train_y, test_y = dataPreProcess.splitTrainTest(
        # 對x進行標準化
        feature=pandas.DataFrame(dataPreProcess.standardized(x)),
        label=y,
        test_percent=0.2,
        stratify=y,
    )
    train_y = numpy.ravel(train_y)

    randomForestFeatureRank(train_x, train_y, test_x, test_y)


if __name__ == "__main__":
    manageFolder("plots")

    data = pandas.DataFrame()
    data = pandas.read_csv("./online_shoppers_intention.csv")

    # feature names
    featureNames = [*data.columns[1:]]

    train_x, train_y, test_x, test_y = (
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
    )

    logger = get_logger("logging")

    main()
