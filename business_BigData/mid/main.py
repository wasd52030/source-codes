import os
import shutil
import calendar
import statistics
from decimal import Decimal, ROUND_HALF_UP
import pandas
import numpy
import seaborn
from matplotlib import pyplot
from sklearn.preprocessing import RobustScaler, StandardScaler
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc


def manageFolder(name: str):
    if not os.path.exists(f'./{name}'):
        os.mkdir(f'./{name}')
    else:
        shutil.rmtree(f'./{name}')  # 等效於 rm -rf ./name
        os.mkdir(f'./{name}')


def pieCharFormatter(pct: float, value: float):
    absolute = int(numpy.round(pct/100.*numpy.sum(value)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def describe(sample: pandas.Series):
    # 平均數,中位數,眾數,全距,四分位距(IQR),四分位差(QD),平均絕對離差(MAD),
    # 樣本變異數(s^2),樣本標準差(s),P20,P25(Q1),P50(Q2),P75(Q3),P80,變異係數(CV)
    Descirbes = {
        "平均數": statistics.mean(sample),
        "中位數": statistics.median(sample),
        "眾數": statistics.mode(sample),
        "全距": sample.max()-sample.min(),
        "四分位距": sample.quantile(.75)-sample.quantile(.25),
        "四分位差": (sample.quantile(.75)-sample.quantile(.25))/2,
        "平均絕對離差": sample.mad(),
        "變異數": statistics.variance(sample),
        "標準差": statistics.stdev(sample),
        "變異係數": statistics.stdev(sample)/statistics.mean(sample),
        "P20": sample.quantile(.2),
        "P25(Q1)": sample.quantile(.25),
        "P50(Q2)": sample.quantile(.5),
        "P75(Q3)": sample.quantile(.75),
        "P85": sample.quantile(.85),
        # 皮爾生偏態係數(SKP)
        "偏態係數": (3*(statistics.mean(sample)-statistics.median(sample))) / statistics.stdev(sample),
        # 峰度係數(ck)
        "峰度係數": sample.kurt(),
    }

    return {
        k: Decimal(v).quantize(Decimal(".00"), ROUND_HALF_UP)
        for k, v in Descirbes.items()
    }  # 針對value做四捨五入到小數點第二位


# 新增3個欄位
# 建立每筆資料的
# 銷售成本(單位成本 x 銷售數量)
# 銷售收入 (單位售價 x 銷售數量)
# 收益 (銷售收入 - 銷售成本)。
def salesData():
    global data_ok

    costs = [row['單位成本']*row['銷售數量'] for _, row in data_ok.iterrows()]
    proceeds = [row['單位售價']*row['銷售數量'] for _, row in data_ok.iterrows()]
    benfit = [proceeds[i]-costs[i] for i in range(len(costs))]

    data_ok['銷售成本'] = costs
    data_ok['銷售收入'] = proceeds
    data_ok['收益'] = benfit

    data_ok.to_csv("./tables/Online_Sales.csv", index=False, encoding="utf8")

    print("銷售成本、銷售收入、收益已計算完成，隨同原本的資料一起存成 ./tables/Online_Sales.csv！")


# 分析商品種類的分佈、特徵、及資料變異等視覺化分析。
def hist_commodityType():
    global data_ok

    commodity_types = list(set(data_ok['商品種類'].values))
    types_count = [
        len(data_ok['商品種類'][(data["商品種類"] == i)]) for i in commodity_types
    ]

    _ = pyplot.figure(figsize=(10, 8))
    pyplot.barh(commodity_types, types_count)
    pyplot.xlabel('商品種類')
    pyplot.savefig("./plots/hist_commodity-type")
    pyplot.cla()
    print("商品種類長條圖已存於./plots/hist_commodity-type.png！")

    for i in commodity_types:
        result = pandas.DataFrame(
            {
                "銷售成本": describe(data_ok["銷售成本"][(data_ok["商品種類"] == i)]),
                "銷售收入": describe(data_ok["銷售收入"][(data_ok["商品種類"] == i)]),
                "收益": describe(data_ok["收益"][(data_ok["商品種類"] == i)])
            }
        )
        result.to_csv(f"./tables/describe_{i}.csv")
        print(f"./tables/describe_{i}.csv OK！")


# 單位售價正規化: 採用RobustScaler和StandardScaler
def unitPrice_Normalization():
    global data_ok

    d = data_ok.drop(
        labels=[
            i for i in data_ok.columns if i not in ['銷售數量', '單位成本', '單位售價']
        ],
        axis=1
    )
    robust = RobustScaler().fit(d)
    robust_scaled = robust.transform(d)
    standard = StandardScaler().fit(d)
    standard_scaled = standard.transform(d)

    seaborn.histplot(robust_scaled[:, 2], kde=True)
    pyplot.savefig("./plots/unitPrice_Normalization-RobustScaler")
    pyplot.cla()
    seaborn.histplot(standard_scaled[:, 2], kde=True)
    pyplot.savefig("./plots/unitPrice_Normalization-StandardScaler")
    pyplot.cla()
    print("採用RobustScaler對單位售價的正規化的製圖已存於 ./plots/unitPrice_Normalization-RobustScaler.png！")
    print("採用StandardScaler對單位售價的正規化的製圖已存於 ./plots/unitPrice_Normalization-StandardScaler.png！")


# 收益正規化: 採用MinMaxScaler和MaxAbsScaler
def revenue_Normalization():
    global data_ok

    d = data_ok.drop(
        labels=[i for i in data_ok.columns if i not in ['銷售成本', '銷售收入', '收益']],
        axis=1
    )
    minMax = MinMaxScaler().fit(d)
    minMax_scaled = minMax.transform(d)
    maxAbs = MaxAbsScaler().fit(d)
    maxAbsScaler_scaled = maxAbs.transform(d)

    seaborn.histplot(minMax_scaled[:, 2], kde=True)
    pyplot.savefig("./plots/revenue_Normalization-MinMaxScaler")
    pyplot.cla()
    seaborn.histplot(maxAbsScaler_scaled[:, 2], kde=True)
    pyplot.savefig("./plots/revenue_Normalization-MaxAbsScaler")
    pyplot.cla()

    print("採用MinMaxScaler對收益的正規化的製圖已存於 ./plots/revenue_Normalization-MinMaxScaler.png！")
    print("採用MaxAbsScaler對收益的正規化的製圖已存於 ./plots/revenue_Normalization-MaxAbsScaler.png！")


def saleCostAnalyze():
    global data_ok

    # 男性與女性銷售總額的比率為何?
    salecost_bysex = [
        sum(data_ok['銷售收入'][(data_ok['性別'] == 'M')].values),
        sum(data_ok['銷售收入'][(data_ok['性別'] == 'F')].values)
    ]
    pyplot.pie(
        salecost_bysex,
        labels=["M", "F"],
        autopct="%0.2f%%"
    )
    pyplot.xlabel('男性與女性銷售總額的比率')
    pyplot.savefig("./plots/salecost_bysex")
    pyplot.cla()
    print("男性與女性銷售總額的比率的製圖已存於 ./plots/salecost_bysex.png！")

    # 哪一個國家的男性總銷售金額最高?
    man_salecost_byconturies = [
        sum(data_ok['銷售收入'][(data_ok['性別'] == 'M') & (data_ok['國別'] == i)].values) for i in list(set(data_ok['國別']))
    ]
    pyplot.pie(
        man_salecost_byconturies,
        labels=list(set(data_ok['國別'])),
        autopct=lambda pct: pieCharFormatter(pct, man_salecost_byconturies)
    )
    pyplot.xlabel('各國男性銷售總額的比率')
    pyplot.savefig("./plots/man_salecost_byconturies")
    pyplot.cla()
    print("各國男性銷售總額的比率的製圖已存於 ./plots/man_salecost_byconturies.png！")

    # 法國男性與女性銷售總額的比率為何
    france_salecost = [
        sum(data_ok['銷售收入'][(data_ok['性別'] == 'M') & (data_ok['國別'] == 'France')].values),
        sum(data_ok['銷售收入'][(data_ok['性別'] == 'F') & (data_ok['國別'] == 'France')].values)
    ]
    pyplot.pie(
        france_salecost,
        labels=["M", "F"],
        autopct="%0.2f%%"
    )
    pyplot.xlabel('法國男性與女性銷售總額的比率')
    pyplot.savefig("./plots/france_salecost")
    pyplot.cla()
    print("法國男性與女性銷售總額的比率的製圖已存於 ./plots/france_salecost.png！")

    # 哪一個國家的總銷售金額最高?
    salecost_byconturies = [
        sum(data_ok['銷售收入'][(data_ok['國別'] == i)].values) for i in list(set(data_ok['國別']))
    ]
    pyplot.pie(
        salecost_byconturies,
        labels=list(set(data_ok['國別'])),
        autopct=lambda pct: pieCharFormatter(pct, salecost_byconturies)
    )
    pyplot.xlabel('各國銷售總額的比率')
    pyplot.savefig("./plots/salecost_byconturies")
    pyplot.cla()
    print("各國銷售總額的比率的製圖已存於 ./plots/salecost_byconturies.png！")


# 5.根據顧客是否會回購，使用DecisionTreeClassifier建立預測分類器，取得其預測的結果(評估)
# 在此以ROC(Receiver Operating Characteristics)呈現
def repoClassifier():
    global data_ok

    x = pandas.DataFrame()
    x['年紀'] = data_ok['年紀']
    x['性別'] = LabelEncoder().fit_transform(data_ok['性別'])
    x['國別'] = LabelEncoder().fit_transform(data_ok['國別'])
    x['商品種類'] = LabelEncoder().fit_transform(data_ok['商品種類'])
    x['商品次分類'] = LabelEncoder().fit_transform(data_ok['商品次分類'])
    x['銷售數量'] = data_ok['銷售數量']
    x['單位成本'] = data_ok['單位成本']
    x['單位售價'] = data_ok['單位售價']

    y = pandas.DataFrame()
    y['回購'] = LabelEncoder().fit_transform(data_ok['回購'])

    # 切測試資料與訓練資料，這邊比率為 訓練:測試=7:3
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.3)

    clf = tree.DecisionTreeClassifier()
    repo_clf = clf.fit(train_x, train_y)
    y_predicted = repo_clf.predict_proba(test_x)

    fpr, tpr, threshold = roc_curve(test_y['回購'], y_predicted[:, 1])
    repo_auc = auc(fpr, tpr)

    # Plot the ROC
    pyplot.figure(figsize=(10, 8))
    pyplot.plot(fpr, tpr, color='orange', label='AUC = %0.2f' % repo_auc)
    pyplot.plot([0, 1], [0, 1], 'r--')
    pyplot.xlim([0, 1])
    pyplot.ylim([0, 1])
    pyplot.ylabel('True Positive Rate')
    pyplot.xlabel('False Positive Rate')
    pyplot.legend(loc="lower right")
    pyplot.title('Receiver Operating Characteristics')
    pyplot.savefig("./plots/ROC")
    pyplot.cla()
    print("根據顧客是否會回購，使用DecisionTreeClassifier建立預測分類器")
    print("將結果整理所製成的ROC(Receiver Operating Characteristics)已存於 ./plots/ROC.png！")


if __name__ == "__main__":

    pyplot.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    pyplot.rcParams['axes.unicode_minus'] = False

    manageFolder('plots')
    manageFolder('tables')

    data = pandas.read_excel("./Online_Sale.xlsx")
    data_ok = data[
        (data['年'] > 1)
        & (data['月'].isin(list(calendar.month_name[1:])))
        & (data['年紀'] > 0)
        & (data['性別'].isin(["M", "F"]))
        & (data['銷售數量'] > 0)
        & (data['單位成本'] > 0)
        & (data['單位售價'] > 0)
        & (data['回購'].isin(["Y", "N"]))
    ]
    data_ok = data_ok.dropna()

    salesData()
    hist_commodityType()
    unitPrice_Normalization()
    revenue_Normalization()
    saleCostAnalyze()
    repoClassifier()
