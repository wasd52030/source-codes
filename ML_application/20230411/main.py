import numpy
import pandas
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot
from matplotlib.colors import ListedColormap
from dataPreProcess import dataPreProcess


def plotDecisionRegions(x, y, classifier, resolution=0.02):
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(numpy.unique(y))])
    x1_min, x1_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    x2_min, x2_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx1, xx2 = numpy.meshgrid(
        numpy.arange(x1_min, x1_max, resolution),
        numpy.arange(x2_min, x2_max, resolution),
    )
    Z = classifier.predict(numpy.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    pyplot.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    pyplot.xlim(xx1.min(), xx1.max())
    pyplot.ylim(xx2.min(), xx2.max())
    for i, cl in enumerate(numpy.unique(y)):
        pyplot.scatter(
            x=x[y == cl, 0],
            y=x[y == cl, 1],
            alpha=0.8,
            c=colors[i],
            marker=markers[i],
            label=cl,
            edgecolor="black",
        )


def main():
    data = pandas.read_csv("./online_shoppers_intention.csv")

    # 去空值
    data = dataPreProcess.removeNullByRow(data)

    # Label Encode
    data = dataPreProcess.labelEncoding(data)

    # 切訓練與測試資料
    x = data[["ProductRelated", "ProductRelated_Duration"]].values
    y = data.iloc[:, data.shape[1] - 1].values
    train_x, test_x, train_y, test_y = dataPreProcess.splitTrainTest(
        # 對x進行標準化
        feature=dataPreProcess.standardized(x),
        label=y,
        test_percent=0.1,
        stratify=y,
    )
    train_y = numpy.ravel(train_y)

    # 建立Logistic Regression模型
    classifiedModel = LogisticRegression(
        C=100, random_state=1, solver="lbfgs", multi_class="ovr"
    )

    # 訓練模型
    classifiedModel.fit(train_x, train_y)

    print(f"訓練集: {classifiedModel.score(train_x, train_y)}")
    print(f"測試集: {classifiedModel.score(test_x, test_y)}")

    x_combined_std = numpy.vstack((train_x, test_x))
    y_combined = numpy.hstack((train_y, test_y))
    plotDecisionRegions(x=x_combined_std, y=y_combined, classifier=classifiedModel)
    pyplot.xlabel("Feature 1")
    pyplot.ylabel("Feature 2")
    pyplot.legend(loc="upper left")
    pyplot.show()


if __name__ == "__main__":
    main()
