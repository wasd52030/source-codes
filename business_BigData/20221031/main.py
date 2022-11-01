import os
import pandas
import calendar
import seaborn
from matplotlib import pyplot
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler


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

    # data_ok.to_csv("./Online_Sales.csv", index=False, encoding="utf8")


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
    pyplot.savefig("./plots/unitPrice_Normalization-RobustScaler.png")
    pyplot.cla()
    seaborn.histplot(standard_scaled[:, 2], kde=True)
    pyplot.savefig("./plots/unitPrice_Normalization-StandardScaler.png")
    pyplot.cla()


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
    pyplot.savefig("./plots/revenue_Normalization-MinMaxScaler.png")
    pyplot.cla()
    seaborn.histplot(maxAbsScaler_scaled[:, 2], kde=True)
    pyplot.savefig("./plots/revenue_Normalization-MaxAbsScaler.png")
    pyplot.cla()


# 分析商品種類的分佈、特徵、及資料變異等視覺化分析。
def hist_commodityType():
    global data_ok
    commodity_types = list(set(data_ok['商品種類'].values))
    types_count = [
        len(data_ok['商品種類'][(data["商品種類"] == commodity_types[0])]),
        len(data_ok['商品種類'][(data["商品種類"] == commodity_types[1])]),
        len(data_ok['商品種類'][(data["商品種類"] == commodity_types[2])])
    ]

    _ = pyplot.figure(figsize=(13.3, 7.5))
    pyplot.barh(commodity_types, types_count)
    pyplot.xlabel('商品種類')
    pyplot.savefig("./plots/hist_commodity-type.png")
    pyplot.cla()


if __name__ == "__main__":

    pyplot.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    pyplot.rcParams['axes.unicode_minus'] = False

    if not os.path.exists('./plots'):
        os.mkdir('./plots')

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
