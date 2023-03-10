# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MentC.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    global l
    l = ['date', 'task']

    def show_date(self, date):
        # Store the selected date in a variable
        selected_date = date.toString()
        l[0] = selected_date

    def task(self):
        t = self.textEdit.toPlainText()
        l[1] = t
        if t == '':
            Form.close()
            return 0
        f = open("remaind.csv", "a+", newline='')
        import csv
        writer = csv.writer(f)
        writer.writerow(l)
        f.close()
        Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 720)
        Form.setMinimumSize(QtCore.QSize(480, 720))
        Form.setMaximumSize(QtCore.QSize(480, 720))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("background: rgb(134,186,212)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 190, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background: rgb(255,255,255);")
        self.textEdit.setObjectName("textEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 330, 445, 250))
        self.calendarWidget.setStyleSheet("background: rgb(255,255,255);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(255,255,255);")
        self.calendarWidget.clicked.connect(self.show_date)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 610, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background:rgba(185,215,230);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background:rgba(0,0,0);\n"
"color: rgb(255,255,255);\n"
"border-radius: 10px;\n"

"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.task)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Remainder"))
        self.label_2.setText(_translate("Form", "Task"))
        self.label_3.setText(_translate("Form", "Due Date"))
        self.pushButton.setText(_translate("Form", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
