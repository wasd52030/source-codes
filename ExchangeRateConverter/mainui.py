# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'designermRMIob.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(472, 372)
        Form.setFixedSize(472, 372)
        self.spinBox1 = QDoubleSpinBox(Form)
        self.spinBox1.setObjectName(u"spinBox1")
        self.spinBox1.setGeometry(QRect(150, 90, 171, 41))
        self.lbl1 = QLabel(Form)
        self.lbl1.setObjectName(u"lbl1")
        self.lbl1.setGeometry(QRect(105, 155, 200, 30))
        self.comboBox1 = QComboBox(Form)
        self.comboBox1.setObjectName(u"comboBox1")
        self.comboBox1.setGeometry(QRect(150, 150, 161, 41))
        self.lbl2 = QLabel(Form)
        self.lbl2.setObjectName(u"lbl2")
        self.lbl2.setGeometry(QRect(95, 255, 200, 30))
        self.comboBox2 = QComboBox(Form)
        self.comboBox2.setObjectName(u"comboBox2")
        self.comboBox2.setGeometry(QRect(150, 250, 161, 41))
        self.lbl3 = QLabel(Form)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(150, 25, 200, 30))
        self.lbl4 = QLabel(Form)
        self.lbl4.setObjectName(u"lbl4")
        self.lbl4.setGeometry(QRect(200, 315, 200, 30))
        self.btn1 = QPushButton(Form)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(185, 200, 90, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "簡易匯率換算器", None))
        self.lbl1.setText(QCoreApplication.translate("Form", "自", None))
        self.lbl2.setText(QCoreApplication.translate("Form", "轉換成", None))
        self.lbl3.setText(QCoreApplication.translate("Form", "資料來源：https://tw.rter.info", None))
        self.lbl4.setText(QCoreApplication.translate("Form", "0", None))
        self.btn1.setText(QCoreApplication.translate("Form", "⇅", None))
    # retranslateUi
