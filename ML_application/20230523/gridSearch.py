import json
import re

import pandas

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from dataPreProcess import dataPreProcess
from utils import (
    Logger,
    get_logger,
)

from typing import List, Dict, Any


def gridSearch(paramGrid: List[Dict[str, Any]]):
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
    modelName = str(paramGrid["model"][0].__class__)[1:-2].split(".")[-1]
    result = {}
    for k, v in grid_search.best_params_.items():
        param = re.findall("(.*)__(.*)", k)
        if len(param) != 0:
            key = param[0][1]
            result[key] = v

    if modelName == "SVC":
        result["kernel"] = paramGrid["model"][0].kernel

    result["model"] = modelName
    result["score"] = grid_search.best_score_

    results.append(result)


@Logger("")
def main():
    global x, y, results

    paramGrids = [
        {
            "model": [LogisticRegression()],
            "model__C": [0.01, 0.1, 1, 10, 100],
            "model__random_state": [0.01, 0.1, 1, 10, 100],
            "model__solver": [
                "lbfgs",
                "liblinear",
                "newton-cg",
                "newton-cholesky",
                "sag",
                "saga",
            ],
            "model__multi_class": ["auto", "ovr", "multinomial"],
            "model__penalty": ["l1", "l2", "elasticnet"],
        },
        {
            "model": [DecisionTreeClassifier()],
            "model__criterion": ["gini", "entropy", "log_loss"],
            "model__random_state": [0.01, 0.1, 1, 10, 100],
            "model__max_depth": [4, 8, 10],
            "model__min_samples_split": [0.01, 0.1, 1, 10, 100],
            "model__splitter": ["best", "random"],
        },
        {
            "model": [SVC()],
            "model__random_state": [0.01, 0.1, 1, 10, 100],
            "model__C": [0.01, 0.1, 1, 10, 100],
            "model__gamma": [0.01, 0.1, 1, 10, 100],
        },
    ]

    for paramGrid in paramGrids:
        Logger(str(paramGrid["model"][0].__class__)[1:-2].split(".")[-1])(gridSearch)(
            paramGrid
        )

    json.dump(
        {"results": results},
        open("./tables_and_reports/gridSearchBestParams.json", "w"),
    )


if __name__ == "__main__":
    results = []

    data = pandas.DataFrame()
    data = pandas.read_csv("./online_shoppers_intention.csv")

    # 去空值
    data = dataPreProcess.removeNullByRow(data)

    # Label Encode
    data = dataPreProcess.labelEncoding(data)

    # 上次用random forest跑出來最有相關性三個的feature
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
