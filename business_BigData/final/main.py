import os
import shutil
import logging
import inspect
import pandas
import numpy
import seaborn
from matplotlib import pyplot
import plotly.express as plotly_express
from utils import manageFolder, Logger


class Analyzer:
    def __init__(self, data: pandas.DataFrame) -> None:
        self.data = data

        self.data['sales_revenue'] = [
            row['Sales']*row['Quantity']*row['Discount'] for _, row in data_ok.iterrows()
        ]

        self.cateGory_types = list(set(self.data['Category'].values))
        self.subCateGory_types = list(set(self.data['Sub-Category'].values))

        # 給magic method之外的method自動打上Logger Decorator
        for method in dir(self):
            m = getattr(self, method)
            if inspect.ismethod(m) and not method.startswith("_"):
                setattr(self, method, Logger(self.__class__.__name__)(m))

        logging.getLogger('matplotlib').setLevel(logging.INFO)
        self.logger = logging.getLogger()

    def sales_revenue_byCategoryAndSubCategory(self):
        # 依類別與子類別分析銷售總額比率
        sales_revenue_by_cateGory = [
            [sum(self.data['sales_revenue'][(self.data["Category"] == i)]), i] for i in self.cateGory_types
        ]
        fig = plotly_express.pie(
            pandas.DataFrame(
                sales_revenue_by_cateGory,
                columns=['sales_revenue', 'Category']
            ),
            values='sales_revenue',
            title='各產品類別銷售總額的比率',
            names='Category'
        )
        fig.write_image(
            './plots/sales_revenue_bycategory.png',
            width=1024,
            height=768
        )
        self.logger.info("依照產品類別分析銷售總額的比率的製圖已存於 ./plots/sales_revenue_bycategory.png！")

        # 針對每一個類別下面的子類別作銷售總額分析
        for i in self.cateGory_types:
            sales_revenue = [
                [sum(self.data['sales_revenue'][(self.data["Category"] == i) & (self.data['Sub-Category'] == j)]), j] 
                for j in self.subCateGory_types
            ]
            sales_revenue = list(filter(lambda x: x[0] > 0, sales_revenue))
            fig = plotly_express.pie(
                pandas.DataFrame(
                    sales_revenue,
                    columns=['sales_revenue', 'Sub-Category']
                ),
                values='sales_revenue',
                title=f'類別{i}中子類別銷售總額的比率',
                names='Sub-Category'
            )
            fig.write_image(
                f'./plots/sales_revenue_by_{i}_subcategory.png',
                width=1024,
                height=768
            )
            self.logger.info(
                f"產品類別{i}中子類別銷售總額的比率的製圖已存於 ./plots/sales_revenue_by_{i}_subcategory.png！"
            )

    def profit_byCategoryAndSubCategory(self):
        # 依類別與子類別分析收益比率
        sales_revenue_by_cateGory = [
            [sum(self.data['Profit'][(self.data["Category"] == i)]), i] for i in self.cateGory_types
        ]
        fig = plotly_express.pie(
            pandas.DataFrame(
                sales_revenue_by_cateGory,
                columns=['Profit', 'Category']
            ),
            values='Profit',
            title='各產品類別收益的比率',
            names='Category'
        )
        fig.write_image(
            './plots/profit_bycategory.png',
            width=1024,
            height=768
        )
        self.logger.info("依照產品類別分析收益比率的製圖已存於 ./plots/profit_bycategory.png！")

        # 針對每一個類別下面的子類別作銷售總額分析
        for i in self.cateGory_types:
            sales_revenue = [
                [sum(self.data['Profit'][(self.data["Category"] == i) & (self.data['Sub-Category'] == j)]), j] 
                for j in self.subCateGory_types
            ]
            sales_revenue = list(filter(lambda x: x[0] > 0, sales_revenue))
            fig = plotly_express.pie(
                pandas.DataFrame(
                    sales_revenue,
                    columns=['Profit', 'Sub-Category']
                ),
                values='Profit',
                title=f'類別{i}中子類別收益的比率',
                names='Sub-Category'
            )
            fig.write_image(
                f'./plots/Profit_by_{i}_subcategory.png',
                width=1024,
                height=768
            )
            self.logger.info(
                f"產品類別{i}中子類別收益比率的製圖已存於 ./plots/Profit_by_{i}_subcategory.png！"
            )



if __name__ == "__main__":

    pyplot.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    pyplot.rcParams['axes.unicode_minus'] = False

    manageFolder('plots')
    manageFolder('tables')

    data = pandas.read_csv("./[FN] Saledata.csv", encoding="utf-8")
    data_ok = data.dropna()

    analyzer1 = Analyzer(data_ok)
    analyzer1.sales_revenue_byCategoryAndSubCategory()
    analyzer1.profit_byCategoryAndSubCategory()
