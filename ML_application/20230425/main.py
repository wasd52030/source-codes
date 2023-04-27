import numpy
import pandas
from matplotlib import pyplot
from mlxtend.plotting import plot_decision_regions
from sklearn.svm import SVC

from dataPreProcess import dataPreProcess


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
        feature=pandas.DataFrame(dataPreProcess.standardized(x)),
        label=y,
        test_percent=0.1,
        stratify=y,
    )
    train_y = numpy.ravel(train_y)

    # 建立SVM模型
    SVM = SVC(kernel='rbf', random_state=1, gamma=0.1, C=100)

    # 訓練模型
    SVM.fit(train_x, train_y)

    print(f"訓練集: {SVM.score(train_x, train_y)}")
    print(f"測試集: {SVM.score(test_x, test_y)}")

    plot_decision_regions(X=train_x.values, y=train_y, clf=SVM)
    pyplot.xlabel("Feature 1")
    pyplot.ylabel("Feature 2")
    pyplot.legend(loc="upper left")
    pyplot.show()


if __name__ == "__main__":
    main()
