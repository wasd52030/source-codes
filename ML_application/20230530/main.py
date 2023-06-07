import inspect

import pandas

from matplotlib import pyplot
from sklearn.base import BaseEstimator
from sklearn.ensemble import (
    AdaBoostClassifier,
    BaggingClassifier,
    RandomForestClassifier,
)
from sklearn.neighbors import KNeighborsClassifier

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    auc,
)
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


from dataPreProcess import dataPreProcess
from utils import (
    modelScore,
    manageFolder,
    Logger,
    get_logger,
    modelPerformanceMetrics,
    resultOutput,
)

from typing import List, Dict, Any


def gridSearch(paramGrid: List[Dict[str, Any]]) -> BaseEstimator:
    global results, train_x, test_x, train_y, test_y

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("pca", PCA(n_components=2)),
            ("model", None),
        ]
    )

    grid_search = GridSearchCV(
        estimator=pipeline, param_grid=paramGrid, scoring="accuracy", cv=5, n_jobs=-1
    )

    grid_search.fit(train_x, train_y)

    # 最佳參數模型
    return grid_search.best_estimator_


def performanceMetrics(pipeline: object, train: bool):
    global logger, results, train_x, test_x, train_y, test_y

    pipeline.fit(train_x, train_y)
    predY = pipeline.predict(train_x if train else test_x)
    accuracyScore = accuracy_score(y_true=train_y if train else test_y, y_pred=predY)
    precisionScore = precision_score(y_true=train_y if train else test_y, y_pred=predY)
    recallScore = recall_score(y_true=train_y if train else test_y, y_pred=predY)
    f1Score = f1_score(y_true=train_y if train else test_y, y_pred=predY)

    results.append(
        modelPerformanceMetrics(
            pipeline.steps[-1][-1], accuracyScore, precisionScore, recallScore, f1Score
        )
    )


def confusionMatrix(pipeline: object, train: bool):
    global logger, results, train_x, test_x, train_y, test_y

    modelName = str(pipeline.steps[-1][-1].__class__)[1:-2].split(".")[-1]

    pipeline.fit(train_x, train_y)
    predY = pipeline.predict(train_x if train else test_x)
    confMat = confusion_matrix(y_true=train_y if train else test_y, y_pred=predY)

    fig, ax = pyplot.subplots(figsize=(5, 5))
    ax.matshow(confMat, cmap=pyplot.cm.Oranges)
    for i in range(confMat.shape[0]):
        for j in range(confMat.shape[1]):
            ax.text(x=j, y=i, s=confMat[i, j], va="center", ha="center")

    pyplot.xlabel("predicted label")
    pyplot.ylabel("true label")
    pyplot.title(f"confusionMatrix_{modelName}_{'train' if train else 'test'}")

    fig.savefig(
        f"./plots/confusionMatrix_{modelName}_{'train' if train else 'test'}.png"
    )
    pyplot.clf()
    pyplot.cla()
    logger.info(f"confusionMatrix_{modelName}_{'train' if train else 'test'} ok！")


@Logger("")
def ROC_AUCs(pipelines: List[object], train: bool):
    global logger, results, train_x, test_x, train_y, test_y

    pyplot.figure(figsize=(10, 6))

    for pipeline in pipelines:
        modelName = str(pipeline.steps[-1][-1].__class__)[1:-2].split(".")[-1]

        if modelName == "SVC":
            pipeline.steps[-1][-1].probability = True

        clf = pipeline.fit(train_x, train_y)
        proba = clf.predict_proba(train_x if train else test_x)[:, -1]
        fpr, tpr, _ = roc_curve(train_y if train else test_y, proba)
        AUC = auc(fpr, tpr)

        pyplot.plot(fpr, tpr, label=f"{modelName} (AUC={AUC:0.2f})")

    pyplot.plot([0, 1], [0, 1], "k--")
    pyplot.xlim([0.0, 1.0])
    pyplot.ylim([0.0, 1.05])
    pyplot.xlabel("False Positive Rate")
    pyplot.ylabel("True Positive Rate")
    pyplot.title(
        f"Receiver Operating Characteristic(ROC)_{'train' if train else 'test'}"
    )
    pyplot.legend(loc="lower right")

    pyplot.savefig(f"./plots/ROC_{'train' if train else 'test'}.png")
    pyplot.clf()
    pyplot.cla()
    logger.info(f"ROC ok！")


@Logger("")
def findBestModel():
    modelPipes = []

    paramGrids = [
        {
            "model": [LogisticRegression()],
            "model__C": [0.01, 0.1, 1, 10, 100],
            "model__random_state": [1, 10, 100],
            "model__solver": [
                "lbfgs",
                "liblinear",
            ],
            "model__multi_class": ["auto", "ovr"],
        },
        {
            "model": [SVC()],
            "model__random_state": [1, 10, 100],
            "model__C": [0.01, 0.1, 1, 10, 100],
            "model__gamma": [0.01, 0.1, 1, 10, 100],
        },
        {
            "model": [DecisionTreeClassifier()],
            "model__criterion": ["gini", "entropy", "log_loss"],
            "model__random_state": [1, 10, 100],
            "model__max_depth": [4, 8, 10],
            "model__min_samples_split": [2, 5, 10, 100],
            "model__splitter": ["best", "random"],
        },
        {
            "model": [RandomForestClassifier()],
            "model__criterion": ["gini", "entropy", "log_loss"],
            "model__random_state": [1, 10, 100],
            "model__max_depth": [4, 8, 10],
            "model__min_samples_split": [2, 5, 10, 100],
            "model__max_features": ["sqrt", "log2"],
        },
        {
            "model": [KNeighborsClassifier()],
            "model__weights": ["uniform", "distance"],
            "model__algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
        },
        {
            "model": [BaggingClassifier()],
            "model__n_estimators": [1, 10, 100],
        },
        {
            "model": [AdaBoostClassifier()],
            "model__n_estimators": [1, 10, 100],
        },
    ]

    for paramGrid in paramGrids:
        modelPipes.append(
            Logger(str(paramGrid["model"][0].__class__)[1:-2].split(".")[-1])(
                gridSearch
            )(paramGrid)
        )

    return modelPipes


def modelsJob():
    global results

    optimizedModels = findBestModel()

    jobs = [confusionMatrix, performanceMetrics]
    for job in jobs:
        for t in [True, False]:
            for i in range(len(optimizedModels)):
                modelname = str(optimizedModels[i].steps[-1][-1].__class__)[1:-2].split(
                    "."
                )[-1]

                Logger(modelname + "_")(job)(optimizedModels[i], t)

            if len(results) != 0:
                resultOutput(
                    f"./tables_and_reports/{job.__name__}_{'train' if t else 'test'}.txt",
                    results,
                )
                results.clear()

    ROC_AUCs(optimizedModels, True)
    ROC_AUCs(optimizedModels, False)


@Logger("")
def main():
    global x, y, results

    modelsJob()


if __name__ == "__main__":
    results = []
    adaboostBanList = ["KNeighborsClassifier"]

    manageFolder("plots")
    manageFolder("tables_and_reports")

    data = pandas.DataFrame()
    data = pandas.read_csv("./online_shoppers_intention.csv")

    # 去空值
    data = dataPreProcess.removeNullByRow(data)

    # Label Encode
    data = dataPreProcess.labelEncoding(data)

    # 上次用random forest跑出來最有相關性的三個feature
    x = data[["PageValues", "ExitRates", "ProductRelated_Duration"]].values
    y = data.iloc[:, data.shape[1] - 1].values

    train_x, test_x, train_y, test_y = dataPreProcess.splitTrainTest(
        feature=x,
        label=y,
        test_percent=0.2,
        stratify=y,
    )

    logger = get_logger("logging")

    main()
