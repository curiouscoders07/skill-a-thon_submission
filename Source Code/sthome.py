# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MentE.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def rema(self):
        subprocess.call(['python', 'remarks.py'])

    def mar(self):
        subprocess.call(['python', 'marks.py'])

    def etar(self):
        subprocess.call(['python', 'editta.py'])

    def fee(self):
        subprocess.call(['python', 'feedb.py'])

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 720)
        Form.setMinimumSize(QtCore.QSize(480, 720))
        Form.setMaximumSize(QtCore.QSize(480, 720))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        Form.setFont(font)
        Form.setStyleSheet("background: rgb(134,186,212);")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 100, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 210, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 550, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 330, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 440, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")

        self.pushButton_5.clicked.connect(self.rema)
        self.pushButton_3.clicked.connect(self.mar)
        self.pushButton.clicked.connect(self.etar)
        self.pushButton_4.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(self.fee)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "View/Edit Target"))
        self.pushButton_3.setText(_translate("Form", "Enter Marks"))
        self.pushButton_4.setText(_translate("Form", "Logout"))
        self.pushButton_5.setText(_translate("Form", "Remark"))
        f=open('sname.txt','r')
        r=f.read()
        f.close()
        self.label.setText(_translate("Form", r))
        self.pushButton_2.setText(_translate("Form", "View Feedback"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
