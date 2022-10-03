import pandas
import numpy
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


# 補空值
def Impute():
    global data
    imputer = SimpleImputer(missing_values=numpy.nan, strategy="median")

    for key in data.keys():
        arg = data[key]
        arg = arg.values.reshape(-1, 1)
        imputer = imputer.fit(arg)
        data[key] = imputer.transform(arg)

    data.to_csv("Imputed_data.csv", index=False)


# 依row標準化
def StandardScale():
    global data
    data_value = data.values
    scaler = StandardScaler().fit(data_value)
    standardScale_result = scaler.transform(data_value)
    with open("./standardScaleByRow_result.txt", "w") as file:
        for item in standardScale_result:
            file.write(f"{numpy.array_str(item)}\n")


if __name__ == "__main__":
    data = pandas.read_csv("C:\[2-1]missing data.csv")
    Impute()
    StandardScale()
