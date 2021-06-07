import requests
import sys
import re
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from mainui import MainUi

r = requests.get('https://tw.rter.info/capi.php')
d = r.json()

# 處理貨幣代號
CurrencyNameLst = [i[3:] for i in d if re.match('USD.*', i) and i[3:] != '']
# 依字母順序排序
CurrencyNameLst.sort()

CurrencyDict = {k: v['Exrate'] for k, v in d.items()}


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainUi()
        self.ui.setupUi(self)
        self.ui.btn1.clicked.connect(self.UpperToLower)
        self.ui.btn2.clicked.connect(self.LowerToUpper)
        self.ui.spinBox1.setMaximum(100000000)
        self.ui.spinBox2.setMaximum(100000000)

    def setcombo(self):
        self.ui.comboBox1.addItems(CurrencyNameLst)
        self.ui.comboBox2.addItems(CurrencyNameLst)

    # 上面輸入框去換下面輸入框
    def UpperToLower(self):
        comb1value = self.ui.comboBox1.currentText()
        comb2value = self.ui.comboBox2.currentText()
        num1value = self.ui.spinBox1.value()
        num2value = self.ui.spinBox2.value()

        if comb2value == 'USD':
            r = num1value/CurrencyDict[f'USD{comb1value}']
            self.ui.spinBox2.setValue(float(r))
        else:
            r = num1value/CurrencyDict[f'USD{comb1value}']
            r *= CurrencyDict[f'USD{comb2value}']
            self.ui.spinBox2.setValue(float(r))

    # 下面輸入框去換上面輸入框
    def LowerToUpper(self):
        comb1value = self.ui.comboBox1.currentText()
        comb2value = self.ui.comboBox2.currentText()
        num1value = self.ui.spinBox1.value()
        num2value = self.ui.spinBox2.value()

        if comb1value == 'USD':
            r = num2value/CurrencyDict[f'USD{comb2value}']
            self.ui.spinBox1.setValue(float(r))
        else:
            r = num2value/CurrencyDict[f'USD{comb2value}']
            r *= CurrencyDict[f'USD{comb1value}']
            self.ui.spinBox1.setValue(float(r))


app = QApplication(sys.argv)
w = MainWindow()
w.setcombo()
w.show()
sys.exit(app.exec_())
