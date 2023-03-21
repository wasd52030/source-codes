import pytest
import pandas
from dataPreProcess import dataPreProcess


@pytest.fixture()
def data() -> pandas.DataFrame:
    return pandas.read_csv("./online_shoppers_intention.csv")


def test_check_null(data):
    print()
    print(dataPreProcess.checkNull(data))


def test_remove_null_by_row(data):
    print()
    print(dataPreProcess.removeNullByRow(data))

def test_get_data_dummies(data):
    print()
    print(dataPreProcess.getDataDummies(data))


def test_standardized(data):
    data=dataPreProcess.getDataDummies(data)

    print()
    print(dataPreProcess.standardized(data))


def test_minmax(data):
    data = dataPreProcess.getDataDummies(data)

    print()
    print(dataPreProcess.minmax(data))


def test_split_train_test(data):
    data = dataPreProcess.getDataDummies(data)

    print()
    print(dataPreProcess.splitTrainTest(data,0.7))
