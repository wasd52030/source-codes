import inspect

import numpy
import pandas

from matplotlib import pyplot

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
from sklearn.model_selection import KFold, cross_val_score


from dataPreProcess import dataPreProcess
from utils import (
    CrossValidation,
    modelScore,
    manageFolder,
    Logger,
    get_logger,
    modelPerformanceMetrics,
    resultOutput,
)

from typing import Callable, List


def modelPipeline(model: object):
    global results, train_x, test_x, train_y, test_y

    modelPipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("pca", PCA(n_components=2)),
            ("model", model),
        ]
    )
    modelPipeline.fit(train_x, train_y)

    results.append(
        modelScore(
            modelPipeline,
            modelPipeline.score(train_x, train_y),
            modelPipeline.score(test_x, test_y),
            f"{inspect.stack()[0][3]}_{str(model.__class__)[1:-2].split('.')[-1]}",
        )
    )


def KFoldCrossValidation(model: object):
    global results, train_x, test_x, train_y, test_y

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("pca", PCA(n_components=2)),
            ("model", model),
        ]
    )

    scores = cross_val_score(
        estimator=pipeline,
        X=train_x,
        y=train_y,
        cv=KFold(n_splits=5),
        n_jobs=2,
    )

    results.append(
        CrossValidation(
            pipeline,
            scores,
            numpy.std(scores),
            numpy.mean(scores),
            f"{inspect.stack()[0][3]}_{str(model.__class__)[1:-2].split('.')[-1]}",
        )
    )


def performanceMetrics(model: object):
    global logger, results, train_x, test_x, train_y, test_y

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("pca", PCA(n_components=2)),
            ("model", model),
        ]
    )

    pipeline.fit(train_x, train_y)
    predY = pipeline.predict(test_x)
    accuracyScore = accuracy_score(y_true=test_y, y_pred=predY)
    precisionScore = precision_score(y_true=test_y, y_pred=predY)
    recallScore = recall_score(y_true=test_y, y_pred=predY)
    f1Score = f1_score(y_true=test_y, y_pred=predY)

    results.append(
        modelPerformanceMetrics(
            model, accuracyScore, precisionScore, recallScore, f1Score
        )
    )


def confusionMatrix(model: object):
    global logger, results, train_x, test_x, train_y, test_y

    modelName = str(model.__class__)[1:-2].split(".")[-1]

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("pca", PCA(n_components=2)),
            ("model", model),
        ]
    )

    pipeline.fit(train_x, train_y)
    predY = pipeline.predict(test_x)
    confMat = confusion_matrix(y_true=test_y, y_pred=predY)

    fig, ax = pyplot.subplots(figsize=(5, 5))
    ax.matshow(confMat, cmap=pyplot.cm.Oranges)
    for i in range(confMat.shape[0]):
        for j in range(confMat.shape[1]):
            ax.text(x=j, y=i, s=confMat[i, j], va="center", ha="center")

    pyplot.xlabel("predicted label")
    pyplot.ylabel("true label")
    pyplot.title(f"confusionMatrix_{modelName}")

    fig.savefig(f"./plots/confusionMatrix_{modelName}.png")
    pyplot.clf()
    pyplot.cla()
    logger.info(f"confusionMatrix_{modelName} ok！")


@Logger("")
def ROC_AUCs(models: List[object]):
    global logger, results, train_x, test_x, train_y, test_y

    pyplot.figure(figsize=(10, 6))

    for model in models:
        modelName = str(model.__class__)[1:-2].split(".")[-1]

        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("pca", PCA(n_components=2)),
                ("model", model),
            ]
        )

        clf = pipeline.fit(train_x, train_y)
        proba = clf.predict_proba(test_x)[:, -1]
        fpr, tpr, _ = roc_curve(test_y, proba)
        AUC = auc(fpr, tpr)

        pyplot.plot(fpr, tpr, label=f"{modelName} (AUC={AUC:0.2f})")

    pyplot.plot([0, 1], [0, 1], "k--")
    pyplot.xlim([0.0, 1.0])
    pyplot.ylim([0.0, 1.05])
    pyplot.xlabel("False Positive Rate")
    pyplot.ylabel("True Positive Rate")
    pyplot.title("Receiver Operating Characteristic(ROC)")
    pyplot.legend(loc="lower right")

    pyplot.savefig(f"./plots/ROC.png")
    pyplot.clf()
    pyplot.cla()
    logger.info(f"ROC ok！")


def originModelJob():
    global x, y, results

    originModels = [
        LogisticRegression(C=100, random_state=1, solver="lbfgs", multi_class="ovr"),
        DecisionTreeClassifier(criterion="gini", random_state=1, max_depth=4),
        SVC(kernel="rbf", random_state=1, gamma=0.1, C=100),
    ]

    jobs = [modelPipeline, KFoldCrossValidation]

    for job in jobs:
        for i in range(len(originModels)):
            Logger(str(originModels[i].__class__)[1:-2].split(".")[-1])(job)(
                originModels[i]
            )

        if len(results) != 0:
            resultOutput(f"./tables_and_reports/origin_{job.__name__}.txt", results)
            results.clear()


def optimizedModelsJob():
    global x, y, results

    optimizedModels = [
        LogisticRegression(
            C=1, random_state=100, solver="saga", multi_class="auto", penalty="l1"
        ),
        DecisionTreeClassifier(
            criterion="entropy",
            random_state=1,
            max_depth=4,
            min_samples_split=0.01,
            splitter="best",
        ),
        SVC(kernel="rbf", random_state=1, gamma=10, C=0.1, probability=True),
    ]

    jobs = [confusionMatrix, performanceMetrics]
    for job in jobs:
        for i in range(len(optimizedModels)):
            Logger(str(optimizedModels[i].__class__)[1:-2].split(".")[-1])(job)(
                optimizedModels[i]
            )

        if len(results) != 0:
            resultOutput(f"./tables_and_reports/optimized_{job.__name__}.txt", results)
            results.clear()

    ROC_AUCs(optimizedModels)


@Logger("")
def main():
    global x, y, results

    originModelJob()
    optimizedModelsJob()


if __name__ == "__main__":
    results = []

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
