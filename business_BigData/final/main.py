import os
import shutil
import calendar
import pandas
import numpy
import seaborn
from matplotlib import pyplot

if __name__ == "__main__":

    pyplot.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    pyplot.rcParams['axes.unicode_minus'] = False

    data=pandas.read_csv("./[FN] Saledata.csv")
    data_ok=data.dropna()
