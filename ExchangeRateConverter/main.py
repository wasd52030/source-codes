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
        self.ui.btn1.clicked.connect(self.switchbm)
        self.ui.spinBox1.setMinimum(1)
        self.ui.spinBox1.setMaximum(100000000)
        self.ui.spinBox1.valueChanged.connect(self.exchange)
        self.ui.comboBox1.currentIndexChanged.connect(self.exchange)
        self.ui.comboBox2.currentIndexChanged.connect(self.exchange)
        self.setcombo()

    def setcombo(self):
        self.ui.comboBox1.addItems(CurrencyNameLst)
        self.ui.comboBox2.addItems(CurrencyNameLst)

    def switchbm(self):
        comb1index = self.ui.comboBox1.currentIndex()
        comb2index = self.ui.comboBox2.currentIndex()
        self.ui.comboBox1.setCurrentIndex(comb2index)
        self.ui.comboBox2.setCurrentIndex(comb1index)

    def exchange(self):
        comb1value = self.ui.comboBox1.currentText()
        comb2value = self.ui.comboBox2.currentText()
        r = self.ui.spinBox1.value()
        if r == '':
            self.ui.sipnBox1.setValue(1)

        if comb2value == 'USD':
            r /= CurrencyDict[f'USD{comb1value}']
            self.ui.lbl4.setText(str(r))
        else:
            r /= CurrencyDict[f'USD{comb1value}']
            r *= CurrencyDict[f'USD{comb2value}']
            self.ui.lbl4.setText('{:.2f}'.format(r))


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
