import numpy
import pandas
from matplotlib import pyplot
from sklearn.cluster import KMeans


def clusteringAnalysis(data: pandas.DataFrame):
    global CountryCode
    # ['Germany','United Kingdom','France','Italy']
    sample = pandas.DataFrame({
        'Country': data['Country'],
        'TotalCost': data['TotalCost'],
        'CountryCode': data['CountryCode']
    })
    sample = sample[
        sample['Country'].isin(
            ['Germany', 'United Kingdom', 'France', 'Italy']
        )
    ]

    cl = []
    for i in sample['TotalCost'].values:
        if i > sample['TotalCost'].quantile(.75):
            cl.append(3)
        elif i > sample['TotalCost'].quantile(.50) and i <= sample['TotalCost'].quantile(.75):
            cl.append(2)
        else:
            cl.append(1)
    sample['CostLevel'] = cl

    X = numpy.array([[row['CountryCode'], row['CostLevel']]
                    for _, row in sample.iterrows()])

    kmeans = KMeans(n_clusters=4, random_state=15).fit(X)
    print(kmeans)
    print(kmeans.labels_)
    k_pred = kmeans.predict([[5, 1], [14, 3]])
    print(k_pred)
    print(kmeans.cluster_centers_)
    print(type(kmeans.cluster_centers_))
    pyplot.scatter(X[:, 0], X[:, 1])
    pyplot.show()


if __name__ == "__main__":

    pyplot.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    pyplot.rcParams['axes.unicode_minus'] = False

    data = pandas.read_excel("./Online_Retail10k.xlsx")
    data_ok = data[
        (data['InvoiceNo'].astype('str').str.isdigit())
        & (data['StockCode'].astype('str').str.isdigit())
        & (data['Quantity'] > 0)
        & (data['UnitPrice'] > 0)
    ]
    data_ok = data_ok.dropna()
    # data_ok.to_csv("./tables/output.csv",index=False)

    # 購買金額
    data_ok['TotalCost'] = [
        row['Quantity']*row['UnitPrice'] for _, row in data_ok.iterrows()
    ]

    CountryCode = {
        item: index for index, item in enumerate(list(set(data_ok['Country'])))
    }
    data_ok['CountryCode'] = [CountryCode[i] for i in data_ok['Country']]

    clusteringAnalysis(data_ok)
