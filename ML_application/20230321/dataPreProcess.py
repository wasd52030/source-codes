from typing import List

import numpy
import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


class dataPreProcess:
    # 檢查各個column有沒有空值，回傳list
    @staticmethod
    def checkNull(data: pandas.DataFrame) -> List[bool]:
        return [*(data.isnull().any())]

    # 移除有空值的row
    @staticmethod
    def removeNullByRow(data: pandas.DataFrame) -> pandas.DataFrame:
        # 檢查Dataframe有沒有空值
        colNullList = dataPreProcess.checkNull(data)

        # 如果有任何一個欄位有空值的話，則刪除空值所在的row
        if sum([i for i in colNullList if i]) > 1:
            return data.dropna()

        # 如果沒有空值的話直接回傳原始資料
        return data

    # 將類別特徵/Label轉換成Dummy型態
    @staticmethod
    def getDataDummies(data: pandas.DataFrame) -> pandas.DataFrame:
        return pandas.get_dummies(data)

    @staticmethod
    def labelEncoding(data: pandas.DataFrame) -> pandas.DataFrame:
        # 檢查所有column是不是數字型態，不是就把該column Label encode
        for col in data.columns:
            if not (data[col].dtype.kind == 'f' or data[col].dtype.kind == 'i'):
                data[col] = LabelEncoder().fit_transform(data[col])
        return data

    # 特徵縮放: standardized
    @staticmethod
    def standardized(data: pandas.DataFrame) -> numpy.ndarray:
        return StandardScaler().fit_transform(data)

    # 特徵縮放: MinMax
    @staticmethod
    def minmax(data: pandas.DataFrame) -> numpy.ndarray:
        return MinMaxScaler().fit_transform(data)

    # 切train data/test data
    @staticmethod
    def splitTrainTest(data: pandas.DataFrame, percent: float) -> List:
        return train_test_split(data, train_size=percent)
