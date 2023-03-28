import pytest
import pandas
import numpy
from dataPreProcess import dataPreProcess


@pytest.fixture()
def data() -> pandas.DataFrame:
    return pandas.read_csv("./online_shoppers_intention.csv")


def test_check_null(data):
    print()
    # 將檢查結果印出來
    print(dataPreProcess.checkNull(data))


def test_remove_null_by_row(data):
    print()
    t = dataPreProcess.checkNull(data)
    result = dataPreProcess.removeNullByRow(data)
    print(f"data.shape={data.shape}\nresult.shape={result.shape}")
    # 如果前面得到的表中有要drop的row的話，其shape理當不一樣，否則應該一樣
    assert (
        result.shape == data.shape
        if len(set(t)) == 1
        else result.shape != data.shape
    )


def test_get_data_dummies(data):
    print()
    # 將轉成dummies type的資料印出來
    print(dataPreProcess.getDataDummies(data))


def test_label_encoding(data):
    print()
    print(dataPreProcess.labelEncoding(data))


def test_split_train_test(data):
    # LabelEncoding
    data = dataPreProcess.labelEncoding(data)

    train_percent = 0.7
    train, test = dataPreProcess.splitTrainTest(data, train_percent)

    print()
    print(f"train: {train.shape[0] / data.shape[0]}")
    print(f"test: {test.shape[0] / data.shape[0]}")

    # 檢查train data占資料的%數是否與設定的%數相同
    assert train.shape[0] / data.shape[0] == train_percent


def test_standardized(data):
    # LabelEncoding
    data = dataPreProcess.labelEncoding(data)

    print()
    # 把經過處理的資料印出來
    print(dataPreProcess.standardized(data))


def test_minmax(data):
    # LabelEncoding
    data = dataPreProcess.labelEncoding(data)

    print()
    # 把經過處理的資料印出來
    x=dataPreProcess.minmax(data)
    print(x)
