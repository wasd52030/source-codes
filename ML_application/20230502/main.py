from typing import List
import numpy
import pandas
from matplotlib import pyplot
from mlxtend.plotting import plot_decision_regions
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from pydotplus import graph_from_dot_data

from dataPreProcess import dataPreProcess
from utils import Accuracy, manageFolder, Logger, get_logger


@Logger("")
def decisionTree(
    train_x: numpy.ndarray,
    train_y: numpy.ndarray,
    test_x: numpy.ndarray,
    test_y: numpy.ndarray,
    classNames: List[str],
    featureNames: List[str],
):
    global accuracies
    # 建立decision tree模型
    model = DecisionTreeClassifier(criterion="gini", random_state=1, max_depth=4)

    # 訓練模型
    model.fit(train_x, train_y)

    accuracies.append(
        Accuracy(
            model,
            model.score(train_x, train_y),
            model.score(test_x, test_y),
        )
    )
    logger.info(f"decisionTree accuracy ok！")

    pyplot.figure(figsize=(12, 8))
    plot_decision_regions(X=train_x.values, y=train_y, clf=model)
    pyplot.xlabel("Feature 1")
    pyplot.ylabel("Feature 2")
    pyplot.legend(loc="upper left")
    pyplot.savefig("./plots/decisionTree_decisionRegions.png")
    pyplot.clf()
    pyplot.cla()
    logger.info(f"decisionTree_decisionRegions ok！")

    dotData = export_graphviz(
        model,
        filled=True,
        rounded=True,
        class_names=classNames,
        feature_names=featureNames,
        out_file=None,
    )
    graph = graph_from_dot_data(dotData)
    graph.write_png("./plots/decisionTree_TreeView.png")
    pyplot.clf()
    pyplot.cla()
    pyplot.close()
    logger.info(f"decisionTree_TreeView ok！")


@Logger("")
def randomForest(
    train_x: numpy.ndarray,
    train_y: numpy.ndarray,
    test_x: numpy.ndarray,
    test_y: numpy.ndarray,
):
    global accuracies
    # 建立decision tree模型
    model = RandomForestClassifier(
        criterion="gini", n_estimators=25, random_state=1, n_jobs=2
    )

    # 訓練模型
    model.fit(train_x, train_y)

    accuracies.append(
        Accuracy(
            model,
            model.score(train_x, train_y),
            model.score(test_x, test_y),
        )
    )
    logger.info(f"randomForest accuracy ok！")

    pyplot.figure(figsize=(12, 8))
    plot_decision_regions(X=train_x.values, y=train_y, clf=model)
    pyplot.xlabel("Feature 1")
    pyplot.ylabel("Feature 2")
    pyplot.legend(loc="upper left")
    pyplot.savefig("./plots/randomForest_decisionRegions.png")
    pyplot.clf()
    pyplot.cla()
    logger.info(f"randomForest_decisionRegions ok！")


@Logger("")
def KNN(
    train_x: numpy.ndarray,
    train_y: numpy.ndarray,
    test_x: numpy.ndarray,
    test_y: numpy.ndarray,
):
    global accuracies
    # 建立decision tree模型
    model = KNeighborsClassifier(n_neighbors=5, p=2, metric="minkowski")

    # 訓練模型
    model.fit(train_x, train_y)

    accuracies.append(
        Accuracy(
            model,
            model.score(train_x, train_y),
            model.score(test_x, test_y),
        )
    )
    logger.info(f"KNN accuracy ok！")

    pyplot.figure(figsize=(12, 8))
    plot_decision_regions(X=train_x.values, y=train_y, clf=model)
    pyplot.xlabel("Feature 1")
    pyplot.ylabel("Feature 2")
    pyplot.legend(loc="upper left")
    pyplot.savefig("./plots/KNN_decisionRegions.png")
    pyplot.clf()
    pyplot.cla()
    logger.info(f"KNN_decisionRegions ok！")


@Logger("")
def main():
    global accuracies, data, train_x, train_y, test_x, test_y

    # 去空值
    data = dataPreProcess.removeNullByRow(data)

    # Label Encode
    data = dataPreProcess.labelEncoding(data)

    # 切訓練與測試資料
    x = data[["ExitRates", "PageValues"]].values
    y = data.iloc[:, data.shape[1] - 1].values
    train_x, test_x, train_y, test_y = dataPreProcess.splitTrainTest(
        # 對x進行標準化
        feature=pandas.DataFrame(dataPreProcess.standardized(x)),
        label=y,
        test_percent=0.2,
        stratify=y,
    )
    train_y = numpy.ravel(train_y)

    decisionTree(
        train_x, train_y, test_x, test_y, ["Yes", "No"], ["ExitRates", "PageValues"]
    )
    randomForest(train_x, train_y, test_x, test_y)
    KNN(train_x, train_y, test_x, test_y)

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
    manageFolder("plots")

    data = pandas.DataFrame()
    data = pandas.read_csv("./online_shoppers_intention.csv")

    train_x, train_y, test_x, test_y = (
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
    )

    logger = get_logger("logging")

    main()
