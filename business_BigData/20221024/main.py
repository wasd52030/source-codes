import pandas
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth


def associationRules(data):
    custData = [
        list(set(items)) for _, items in data.groupby('CustomerID', as_index=False)['Item Description']
    ]

    t = TransactionEncoder()
    t_arr = t.fit(custData).transform(custData)
    d = pandas.DataFrame(t_arr, columns=t.columns_)
    fpgrowth(
        d,
        min_support=0.01,
        use_colnames=True
    ).to_csv("./itemset.csv")


if __name__ == '__main__':
    data = pandas.read_csv("./Cust_Data.csv")
    data_ok = data[
        ~data['CustomerID'].isna()
        & ~data['SaleDate'].isna()
        & (~data['SaleNum'].isna() & data['SaleNum'].str.isdigit())
        & (~data['Code'].isna() & data['Code'].str.isdigit())
        & ~data['Item Description'].isna()
        & (~data['Quantity'].isna() & data['Quantity'] > 0)
        & (~data['UnitPrice'].isna() & data['UnitPrice'] > 0)
        & ~data['Country'].isna()
    ]
    data_ok.to_csv("./processedData.csv", index=False)
    associationRules(data_ok)
