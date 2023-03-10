# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewRemarks.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import csv

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        with open("mentee.txt") as f:
            a=f.read()
        with open('remark.csv','r') as f:
            reader=csv.reader(f)
            exit=0
            for i in reader:
                if i[0]==a:
                    exit=1
                    text=i[1]
            if exit==0:
                text= 'Remark not available '
        Form.setObjectName("Form")
        Form.resize(480, 720)
        Form.setMinimumSize(QtCore.QSize(480, 720))
        Form.setMaximumSize(QtCore.QSize(480, 720))
        Form.setStyleSheet("background-color: rgb(134,186,212);")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 421, 231))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: rgb(185,215,230)")
        self.label_2.setText(text)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "View Remarks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
