
import logging
import inspect
from datetime import datetime
import pandas
import numpy
from matplotlib import pyplot
import plotly.express as plotly_express
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from darts import TimeSeries
from darts.models import ExponentialSmoothing, Theta
from utils import manageFolder, Logger


class Analyzer:
    def __init__(self, data: pandas.DataFrame) -> None:

        logging.getLogger('matplotlib').setLevel(logging.INFO)
        self.logger = logging.getLogger()

        self.data = data
        self.data = self.data.dropna()
        self.fig = None

        # 單筆訂單顧客所消費的金額(含打折)
        self.data['Price'] = [
            (row['Sales']/row['Quantity'])/row['Discount'] if row['Discount'] > 0 else row['Sales']/row['Quantity']
            for _, row in self.data.iterrows()
        ]

        # ym, y, m = [], [], []
        # for index, item in enumerate(self.data['Order Date'].values):
        #     try:
        #         d = datetime.strptime(item, "%m/%d/%Y")
        #         self.data.loc[index, 'Order Date'] = d
        #         y.append(d.year)
        #         m.append(d.month)
        #     except ValueError:
        #         self.data = self.data.drop(index)
        self.data['Order Date'] = self.data['Order Date'].apply(lambda _: datetime.strptime(_, "%m/%d/%Y"))
        self.data['Order_Year'] = self.data['Order Date'].apply(lambda _: _.year)
        self.data['Order_Month'] = self.data['Order Date'].apply(lambda _: _.month)
        self.data['Order_YearMonth'] = self.data['Order Date'].apply(lambda _: f'{_.year}-{_.month}' if _.month >= 10 else f'{_.year}-0{_.month}')

        # 求回購：檢查客戶ID是否有在2017年購買的紀錄
        start_2017 = datetime.strptime("2017/1/1", "%Y/%m/%d")
        end_2017 = datetime.strptime("2017/12/31", "%Y/%m/%d")
        repurchaseIDs = list(
            set(
                [i for i in self.data['Customer ID'][(self.data['Order Date'] >= start_2017) & (self.data['Order Date'] <= end_2017)]]
            )
        )
        self.data['repurchase'] = [1 if data['Customer ID'][i] in repurchaseIDs else 0 for i in range(self.data.shape[0])]
        self.data = self.data.sort_values(by=['Order Date'])

        self.cateGory_types = list(set(self.data['Category'].values))
        self.subCateGory_types = list(set(self.data['Sub-Category'].values))
        self.Conturies = list(set(self.data['Country'].values))
        # 從上面的Conturies知道，這筆資料只有美國一個國家，所以地區、州別的部分可以把全部的資料取不重複
        self.region = list(set(self.data['Region'].values))
        self.state = list(set(self.data['State'].values))

        # 收益
        manageFolder('./plots/profit')

        # 銷售總額
        manageFolder('./plots/Sales')

        # 銷量
        manageFolder('./plots/quantity')

        # 客戶國家、地區、州別分布
        manageFolder('./plots/contry_region_state')

        # 預測購買
        manageFolder('./plots/sales_predict')

        # 給magic method之外的method自動打上Logger Decorator
        for method in dir(self):
            m = getattr(self, method)
            if inspect.ismethod(m) and not method.startswith("_"):
                setattr(self, method, Logger(self.__class__.__name__)(m))

    # 分析顧客的國家、區域、州別分布
    # Todo: 州別分布尚未製作
    def conturies_and_regions(self):
        self.fig = plotly_express.pie(
            pandas.DataFrame(
                [[len(self.data[(self.data['Country'] == i)]), i] for i in self.Conturies],
                columns=['data', 'Country']
            ),
            values='data',
            title='客戶所屬國家',
            names='Country'
        )
        self.fig.write_image(
            './plots/contry_region_state/customer_countries.png',
            width=1024,
            height=768,
        )
        self.logger.info("客戶所屬國家歸納的製圖已存到 ./plots/contry_region_state/customer_countries.png")

        self.fig = plotly_express.pie(
            pandas.DataFrame(
                [[len(self.data[self.data['Region'] == i]), i] for i in self.region],
                columns=['data', 'Region']
            ),
            values='data',
            title='客戶所屬地區',
            names='Region'
        )
        self.fig.write_image(
            './plots/contry_region_state/customer_regions.png',
            width=1024,
            height=768,
        )
        self.logger.info("客戶所屬地區歸納的製圖已存到 ./plots/contry_region_state/customer_regions.png")

        self.fig = plotly_express.pie(
            pandas.DataFrame(
                [[len(self.data[(self.data['State'] == i)]), i] for i in self.state],
                columns=['data', 'State']
            ),
            values='data',
            title='客戶所屬州',
            names='State'
        )
        self.fig.write_image(
            './plots/contry_region_state/customer_states.png',
            width=1024,
            height=768,
        )
        self.logger.info("客戶所屬州歸納的製圖已存到 ./plots/contry_region_state/customer_states.png")

    # 依據產品的分類和次分類分析銷售額
    def sales_byCategoryAndSubCategory(self):
        # 依類別與子類別分析銷售總額比率
        Sales_by_cateGory = [
            [sum(self.data['Sales'][(self.data["Category"] == i)]), i] for i in self.cateGory_types
        ]
        self.fig = plotly_express.pie(
            pandas.DataFrame(
                Sales_by_cateGory,
                columns=['Sales', 'Category']
            ),
            values='Sales',
            title='各產品類別銷售總額的比率',
            names='Category'
        )
        self.fig.write_image(
            './plots/Sales/Sales_bycategory.png',
            width=1024,
            height=768
        )
        self.logger.info("依照產品類別分析銷售總額的比率的製圖已存於 ./plots/Sales/Sales_bycategory.png！")

        # 針對每一個類別下面的子類別作銷售總額分析
        for i in self.cateGory_types:
            Sales = [
                [sum(self.data['Sales'][(self.data["Category"] == i) & (self.data['Sub-Category'] == j)]), j]
                for j in self.subCateGory_types
            ]
            Sales = list(filter(lambda x: x[0] > 0, Sales))
            self.fig = plotly_express.pie(
                pandas.DataFrame(
                    Sales,
                    columns=['Sales', 'Sub-Category']
                ),
                values='Sales',
                title=f'類別{i}中子類別銷售總額的比率',
                names='Sub-Category'
            )
            self.fig.write_image(
                f'./plots/Sales/Sales_by_{i}_subcategory.png',
                width=1024,
                height=768
            )
            self.logger.info(
                f"產品類別{i}中子類別銷售總額的比率的製圖已存於 ./plots/Sales/Sales_by_{i}_subcategory.png！"
            )

    # 依據產品的分類和次分類分析獲利
    def profit_byCategoryAndSubCategory(self):
        # 依類別與子類別分析收益比率
        profit_by_cateGory = [
            [sum(self.data['Profit'][(self.data["Category"] == i)]), i] for i in self.cateGory_types
        ]
        self.fig = plotly_express.pie(
            pandas.DataFrame(
                profit_by_cateGory,
                columns=['Profit', 'Category']
            ),
            values='Profit',
            title='各產品類別收益的比率',
            names='Category'
        )
        self.fig.write_image(
            './plots/profit/profit_bycategory.png',
            width=1024,
            height=768
        )
        self.logger.info("依照產品類別分析比率的製圖已存於 ./plots/profit/profit_bycategory.png！")

        # 針對每一個類別下面的子類別作收益分析
        for i in self.cateGory_types:
            profit = [
                [sum(self.data['Profit'][(self.data["Category"] == i) & (self.data['Sub-Category'] == j)]), j]
                for j in self.subCateGory_types
            ]
            profit = list(filter(lambda x: x[0] > 0, profit))
            self.fig = plotly_express.pie(
                pandas.DataFrame(
                    profit,
                    columns=['Profit', 'Sub-Category']
                ),
                values='Profit',
                title=f'類別{i}中子類別收益的比率',
                names='Sub-Category'
            )
            self.fig.write_image(
                f'./plots/profit/profit_by_{i}_subcategory.png',
                width=1024,
                height=768
            )
            self.logger.info(
                f"產品類別{i}中子類別收益比率的製圖已存於 ./plots/profit_by_{i}_subcategory.png！"
            )

    # 依據產品的分類和次分類分析銷量
    def quantity_byCategoryAndSubCategory(self):
        # 依類別與子類別分析銷量比率
        quantity_revenue_by_cateGory = [
            [sum(self.data['Quantity'][(self.data["Category"] == i)]), i] for i in self.cateGory_types
        ]
        self.fig = plotly_express.pie(
            pandas.DataFrame(
                quantity_revenue_by_cateGory,
                columns=['Quantity', 'Category']
            ),
            values='Quantity',
            title='各產品類別銷量的比率',
            names='Category'
        )
        self.fig.write_image(
            './plots/quantity/quantity_bycategory.png',
            width=1024,
            height=768
        )
        self.logger.info("依照產品類別分析銷量比率的製圖已存於 ./plots/quantity/quantity_bycategory.png！")

        # 針對每一個類別下面的子類別作銷量總額分析
        for i in self.cateGory_types:
            quantity = [
                [sum(self.data['Quantity'][(self.data["Category"] == i) & (self.data['Sub-Category'] == j)]), j]
                for j in self.subCateGory_types
            ]
            quantity = list(filter(lambda x: x[0] > 0, quantity))
            self.fig = plotly_express.pie(
                pandas.DataFrame(
                    quantity,
                    columns=['Quantity', 'Sub-Category']
                ),
                values='Quantity',
                title=f'類別{i}中子類別銷量的比率',
                names='Sub-Category'
            )
            self.fig.write_image(
                f'./plots/quantity/quantity_by_{i}_subcategory.png',
                width=1024,
                height=768
            )
            self.logger.info(
                f"產品類別{i}中子類別銷量比率的製圖已存於 ./plots/quantity/quantity_by_{i}_subcategory.png！"
            )

    # 針對任一地區(Region)，分析其獲利最高、銷售數量及金額最高的商品(子類別)。
    def sales_data_byRegion(self):
        for i in self.region:
            # 收益(獲利)
            profit = [
                [sum(self.data['Profit'][(self.data["Region"] == i) & (self.data['Sub-Category'] == j)]), j]
                for j in self.subCateGory_types
            ]
            profit = list(filter(lambda x: x[0] > 0, profit))
            self.fig = plotly_express.pie(
                pandas.DataFrame(
                    profit,
                    columns=['Profit', 'Sub-Category']
                ),
                values='Profit',
                title=f'{i}地區中子類別收益的比率',
                names='Sub-Category'
            )
            self.fig.write_image(
                f'./plots/profit/profit_by_{i}_region.png',
                width=1024,
                height=768
            )
            self.logger.info(
                f"{i}地區中子類別收益比率的製圖已存於 ./plots/profit/profit_by_{i}_region.png！"
            )

            # 銷量
            quantity = [
                [sum(self.data['Quantity'][(self.data["Region"] == i) & (self.data['Sub-Category'] == j)]), j]
                for j in self.subCateGory_types
            ]
            quantity = list(filter(lambda x: x[0] > 0, quantity))
            self.fig = plotly_express.pie(
                pandas.DataFrame(
                    quantity,
                    columns=['Quantity', 'Sub-Category']
                ),
                values='Quantity',
                title=f'{i}地區中子類別銷量的比率',
                names='Sub-Category'
            )
            self.fig.write_image(
                f'./plots/quantity/quantity_by_{i}_region.png',
                width=1024,
                height=768
            )
            self.logger.info(
                f"{i}地區中子類別銷量比率的製圖已存於 ./plots/quantity/quantity_by_{i}_region.png！"
            )

            # 銷售額
            Sales = [
                [sum(self.data['Sales'][(self.data["Region"] == i) & (self.data['Sub-Category'] == j)]), j]
                for j in self.subCateGory_types
            ]
            Sales = list(filter(lambda x: x[0] > 0, Sales))
            self.fig = plotly_express.pie(
                pandas.DataFrame(
                    Sales,
                    columns=['Sales', 'Sub-Category']
                ),
                values='Sales',
                title=f'{i}地區中子類別銷售總額的比率',
                names='Sub-Category'
            )
            self.fig.write_image(
                f'./plots/Sales/Sales_by_{i}_region.png',
                width=1024,
                height=768
            )
            self.logger.info(
                f"{i}地區中子類別銷售總額的比率的製圖已存於 ./plots/Sales/Sales_by_{i}_region.png！"
            )

    # 使用前三年的資料(2014~2016)，預測顧客在第四年(2017)會不會來買？
    def predict_repurchase(self):
        x = pandas.DataFrame()
        x['Order_Year'] = self.data['Order_Year']
        x['Order_Month'] = self.data['Order_Month']
        x['Segment'] = LabelEncoder().fit_transform(self.data['Segment'])
        x['City'] = LabelEncoder().fit_transform(self.data['City'])
        x['State'] = LabelEncoder().fit_transform(self.data['State'])
        x['Region'] = LabelEncoder().fit_transform(self.data['Region'])
        x['Category'] = LabelEncoder().fit_transform(self.data['Category'])
        x['Sub-Category'] = LabelEncoder().fit_transform(self.data['Sub-Category'])
        x['Price'] = self.data['Price']
        x['Quantity'] = self.data['Quantity']
        x['Discount'] = self.data['Discount']

        y = pandas.DataFrame()
        y['repurchase'] = self.data['repurchase']

        normal_w = MinMaxScaler().fit(x).transform(x)
        # 切測試資料與訓練資料
        train_x, test_x, train_y, test_y = train_test_split(normal_w, y, test_size=0.7)
        train_y = numpy.ravel(train_y)

        clf = RandomForestClassifier(max_depth=70, random_state=0)
        repo_clf = clf.fit(train_x, train_y)
        y_predicted = repo_clf.predict_proba(test_x)

        fpr, tpr, threshold = roc_curve(test_y['repurchase'], y_predicted[:, 1])
        repo_auc = auc(fpr, tpr)

        # Plot the ROC
        pyplot.figure(figsize=(12, 8))
        pyplot.plot(fpr, tpr, color='orange', label='AUC = %0.2f' % repo_auc)
        pyplot.plot([0, 1], [0, 1], 'r--')
        pyplot.xlim([0, 1])
        pyplot.ylim([0, 1])
        pyplot.ylabel('True Positive Rate')
        pyplot.xlabel('False Positive Rate')
        pyplot.legend(loc="lower right")
        pyplot.title('Receiver Operating Characteristics')
        pyplot.savefig("./plots/sales_predict/ROC")
        pyplot.clf()
        pyplot.cla()
        print(f"根據顧客是否會回購，使用{str(type(clf)).split('.')[-1][:-2]}建立預測分類器")
        print("將結果整理所製成的ROC(Receiver Operating Characteristics)已存於 ./plots/sales_predict/ROC.png！")

    # 使用前三年的資料(2014~2016)，預測顧客在第四年(2017)會買多少錢？
    def predict_Sales(self):
        u = self.data.groupby(['Order_YearMonth'])
        v = u['Sales'].sum().to_frame()
        # reference -> https://stackoverflow.com/questions/71052774/classmethod-from-dataframedf-time-col-none-value-cols-none-fill-missing-date
        v['date'] = pandas.date_range(start='1/1/2014', end='12/31/2017', freq='M')

        # About Time Series -> https://bc165870081.medium.com/%E6%99%82%E9%96%93%E5%BA%8F%E5%88%97%E7%9A%84ai%E4%BB%8B%E7%B4%B9-ff250cfc2ff9
        # reference -> https://unit8co.github.io/darts/README.html
        sample = TimeSeries.from_dataframe(v, time_col='date', value_cols='Sales')
        train, val = sample.split_after(pandas.Timestamp('20170101'))

        modal = ExponentialSmoothing()
        modal.fit(train)
        predicttion = modal.predict(len(val))

        pyplot.figure(figsize=(12, 8))
        sample.plot(label='actual')
        predicttion.plot(label='forecast', lw=3)
        pyplot.legend()
        pyplot.savefig('./plots/sales_predict/sales_predict.png')
        pyplot.clf()
        pyplot.cla()


if __name__ == "__main__":

    pyplot.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    pyplot.rcParams['axes.unicode_minus'] = False

    manageFolder('tables')
    manageFolder('plots')

    data = pandas.read_csv("./[FN] Saledata.csv", encoding="utf-8")

    analyzer1 = Analyzer(data)
    analyzer1.conturies_and_regions()
    analyzer1.sales_byCategoryAndSubCategory()
    analyzer1.profit_byCategoryAndSubCategory()
    analyzer1.quantity_byCategoryAndSubCategory()
    analyzer1.sales_data_byRegion()
    analyzer1.predict_repurchase()
    analyzer1.predict_Sales()