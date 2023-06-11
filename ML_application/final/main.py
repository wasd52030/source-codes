import numpy
import pandas

from matplotlib import pyplot

from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    auc,
)
from sklearn.pipeline import Pipeline
from sklearn.model_selection import (
    GridSearchCV,
    StratifiedKFold,
)


from dataPreProcess import dataPreProcess
from utils import (
    modelPerformanceMetrics,
    manageFolder,
    Logger,
    get_logger,
    resultOutput,
)

from typing import List, Dict, Any


def getPipeLine(model: object) -> Pipeline:
    return Pipeline(
        [
            ("scaler", StandardScaler()),
            ("pca", PCA(n_components=2)),
            ("model", model),
        ]
    )


@Logger("")
def randomForestFeatureRank():
    global data, train_x, train_y, test_x, test_y

    # feature names
    featureNames = [*data.columns[:-1]]

    x = data.iloc[:, :-1].values
    y = data.iloc[:, data.shape[1] - 1].values

    train_x, test_x, train_y, test_y = dataPreProcess.splitTrainTest(
        feature=pandas.DataFrame(dataPreProcess.standardized(x)),
        label=y,
        test_percent=0.2,
        stratify=y,
    )

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
            # "%2d) %-*s %f" % (f + 1, 30, featureNames[inidices[f]], rank[inidices[f]])
            print(
                f"{f + 1:2d}) {featureNames[inidices[f]]:<30s} {rank[inidices[f]]:.4f}",
                file=file,
            )

    featureNames = [featureNames[inidices[f]] for f in range(train_x.shape[1])]
    pyplot.title("Feature Importance")
    pyplot.bar(range(train_x.shape[1]), rank[inidices], align="center")
    pyplot.xticks(range(train_x.shape[1]), featureNames, rotation=90)
    pyplot.xlim([-1, train_x.shape[1]])
    pyplot.tight_layout()
    pyplot.savefig("./plots/featureRank.png")
    pyplot.cla()
    pyplot.clf()
    pyplot.close()

    logger.info(f"featureRank.png ok！")

    return featureNames


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


def findBestModel() -> List[BaseEstimator]:
    global logger, paramGrids

    result = []

    for paramGrid in paramGrids:
        modelName = str(paramGrid["model"][0].__class__)[1:-2].split(".")[-1]
        result.append(Logger(modelName)(gridSearch)(paramGrid))

    return result


def KFoldCrossValidation(model: object, train: bool, modelType=""):
    global results, train_x, test_x, train_y, test_y

    dataType = "train" if train else "test"

    pyplot.figure(figsize=(10, 6))

    X = train_x if train else test_x
    Y = train_y if train else test_y

    if isinstance(model, Pipeline):
        pipeline = model
        modelname = str(model.steps[-1][-1].__class__)[1:-2].split(".")[-1]
    else:
        modelname = str(model.__class__)[1:-2].split(".")[-1]
        pipeline = getPipeLine(model)

    kfold = StratifiedKFold(n_splits=5)

    mean_tpr = 0.0
    mean_fpr = numpy.linspace(0, 1, 101)

    for k, (train, test) in enumerate(kfold.split(X, Y)):
        probas = pipeline.fit(X[train], Y[train]).predict_proba(X[test])
        fpr, tpr, _ = roc_curve(Y[test], probas[:, 1], pos_label=1)
        mean_tpr += numpy.interp(mean_fpr, fpr, tpr)
        roc_auc = auc(fpr, tpr)
        pyplot.plot(fpr, tpr, label="ROC fold %d (area = %0.2f)" % (k + 1, roc_auc))

    mean_tpr /= kfold.get_n_splits()
    mean_tpr[0] = 0.0
    mean_auc = auc(mean_fpr, mean_tpr)
    pyplot.plot(
        mean_fpr,
        mean_tpr,
        label="Mean ROC (area = %0.2f)" % mean_auc,
        linestyle="--",
        lw=2,
    )

    pyplot.plot([0, 1], [0, 1], linestyle="--", color="gray", alpha=0.7)
    pyplot.xlim([0.0, 1.0])
    pyplot.ylim([0.0, 1.05])
    pyplot.xlabel("False Positive Rate")
    pyplot.ylabel("True Positive Rate")
    pyplot.title(
        f"Receiver Operating Characteristic (ROC)_KFoldCrossValidation\n{modelname}{'_'+modelType if modelType!='' else ''}_{dataType}"
    )
    pyplot.legend(loc="lower right")
    pyplot.savefig(
        f"./plots/{modelname}_ROC(KFold){'_'+modelType if modelType!='' else ''}_{dataType}.jpg"
    )
    pyplot.cla()
    pyplot.clf()
    pyplot.close()


def performanceMetrics(model: object, train: bool):
    global logger, results, train_x, test_x, train_y, test_y

    X = train_x if train else test_x
    Y = train_y if train else test_y

    pipeline = getPipeLine(model)
    pipeline.fit(train_x, train_y)
    predY = pipeline.predict(X)

    confMat = confusion_matrix(
        y_true=train_y if train else test_y, y_pred=predY
    ).tolist()
    accuracyScore = accuracy_score(y_true=Y, y_pred=predY)
    precisionScore = precision_score(y_true=Y, y_pred=predY, zero_division=1)
    recallScore = recall_score(y_true=Y, y_pred=predY, zero_division=1)
    f1Score = f1_score(y_true=Y, y_pred=predY, zero_division=1)
    aucScore = roc_auc_score(Y, predY)

    results.append(
        modelPerformanceMetrics(
            model.steps[-1][-1] if hasattr(model, "steps") else model,
            confMat,
            accuracyScore,
            precisionScore,
            recallScore,
            f1Score,
            aucScore,
        )
    )


@Logger("")
def originModelJob():
    global data, paramGrids, train_x, train_y, test_x, test_y, results

    x = data.iloc[:, :-1].values
    y = data.iloc[:, data.shape[1] - 1].values

    train_x, test_x, train_y, test_y = dataPreProcess.splitTrainTest(
        feature=x,
        label=y,
        test_percent=0.2,
        random_state=52,
        stratify=y,
    )

    originModels = [paramGrid["model"][0] for paramGrid in paramGrids]

    jobs = [performanceMetrics, KFoldCrossValidation]
    for job in jobs:
        train = True
        for _ in range(2):
            for model in originModels:
                modelname = str(model.__class__)[1:-2].split(".")[-1]

                Logger(f"origin_{modelname}_")(job)(model, train)

            if len(results) != 0:
                resultOutput(
                    f"./tables_and_reports/{job.__name__}_{'train' if train else 'test'}.txt",
                    results,
                )
                results.clear()

            train = not train


@Logger("")
def optimizedModelsJob():
    global data, train_x, train_y, test_x, test_y, results

    # 特徵關聯排名
    rank = randomForestFeatureRank()

    x = data[rank[:5]].values
    y = data.iloc[:, data.shape[1] - 1].values

    train_x, test_x, train_y, test_y = dataPreProcess.splitTrainTest(
        feature=x,
        label=y,
        test_percent=0.3,
        random_state=52,
        stratify=y,
    )

    models = findBestModel()

    jobs = [performanceMetrics, KFoldCrossValidation]
    for job in jobs:
        train = True
        for _ in range(2):
            for model in models:
                modelname = str(model.steps[-1][-1].__class__)[1:-2].split(".")[-1]

                if job == KFoldCrossValidation:
                    Logger(f"optimized_{modelname}_")(job)(model, train, "optimized")
                else:
                    Logger(f"optimized_{modelname}_")(job)(model, train)

            if len(results) != 0:
                resultOutput(
                    f"./tables_and_reports/{job.__name__}_optimized_{'train' if train else 'test'}.txt",
                    results,
                )
                results.clear()

            train = not train


@Logger("")
def main():
    global x, y, results

    originModelJob()
    optimizedModelsJob()


if __name__ == "__main__":
    results = []

    logger = get_logger("logging")
    manageFolder("plots")
    manageFolder("tables_and_reports")

    data = pandas.DataFrame()
    data = pandas.read_csv("./online_shoppers_intention.csv")

    # 去空值
    data = dataPreProcess.removeNullByRow(data)

    # Label Encode
    data = dataPreProcess.labelEncoding(data)

    train_x, test_x, train_y, test_y = (
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
        numpy.ndarray([1, 2, 3]),
    )

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
            "model": [SVC(probability=True)],
            "model__random_state": [1, 10, 100],
            "model__C": [0.01, 0.1, 1, 10, 100],
            "model__gamma": [0.01, 0.1, 1, 10, 100],
        },
        {
            "model": [DecisionTreeClassifier()],
            "model__criterion": ["gini", "entropy", "log_loss"],
            "model__random_state": [1, 10, 50, 100],
            "model__max_depth": [4, 8, 10],
            "model__min_samples_split": [2, 5, 10, 100],
            "model__splitter": ["best", "random"],
        },
        {
            "model": [RandomForestClassifier()],
            "model__criterion": ["gini", "entropy", "log_loss"],
            "model__random_state": [1, 10, 100],
            "model__max_depth": [4, 5, 8, 10],
            "model__min_samples_split": [2, 5, 10, 100],
            "model__max_features": ["sqrt", "log2"],
        },
        {
            "model": [KNeighborsClassifier()],
            "model__n_neighbors": [1, 2, 5, 10],
            "model__p": [1, 2, 5, 10],
            "model__weights": ["uniform", "distance"],
            "model__algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
        },
    ]

    main()
