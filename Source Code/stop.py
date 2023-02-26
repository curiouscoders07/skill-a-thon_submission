from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_Form(object):
    def main(self):
        if self.flag == True:
            self.count += 1
        s_ = self.count//100
        ms_ = self.count%100
        if ms_<=9:
            ms_ = "0"+str(ms_)
        else:
            ms_ = str(ms_)
        txt = time.strftime('%H:%M:%S', time.gmtime(s_)) +":"+ ms_
        self.n_lbl.setText(txt)
    def StartF(self):
        if self.count1%2 == 0:
            self.Start.setText("Stop")
            self.Reset.setEnabled(True)
            self.Start.setStyleSheet("""border-radius: 10px;
background:rgb(162, 10, 10);
Color: rgb(255, 60, 50);
font: "helvetica";""")
            self.count1 += 1
            self.flag = True
        else:
            self.Start.setText("Start")
            self.Start.setStyleSheet("border-radius: 10px;\n"
"font: \"helvetica\";\n"
"color: rgb(61, 255, 8);\n"
"\n"
"background-color: rgb(20, 132, 1);")
            self.count1 += 1
            self.flag = False
    def Close(self):
        Form.close()
    def minimise(self):
        Form.showMinimized()
    def ResetF(self):
        self.count,self.count1 = 0,0
        self.flag = False
        self.Start.setText("Start")
        self.Reset.setEnabled(False)
        self.Start.setStyleSheet("border-radius: 10px;\n"
"font: \"helvetica\";\n"
"color: rgb(61, 255, 8);\n"
"\n"
"background-color: rgb(20, 132, 1);")
    def setupUi(self, Form):
        self.count = 0
        self.count1 = 0
        Form.setObjectName("Form")
        Form.resize(431, 431)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 431, 431))
        self.frame.setStyleSheet("QFrame{\n"
"background: transparent;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(25, 25, 381, 381))
        self.frame_2.setStyleSheet("QFrame{\n"
"border-radius: 50%;\n"
"background: black;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header = QtWidgets.QLabel(self.frame_2)
        self.header.setGeometry(QtCore.QRect(56, 44, 250, 51))
        font = QtGui.QFont()
        font.setFamily("ROBO")
        font.setPointSize(26)
        self.header.setFont(font)
        self.header.setStyleSheet("color: white;")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.n_lbl = QtWidgets.QLabel(self.frame_2)
        self.n_lbl.setGeometry(QtCore.QRect(60, 160, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.n_lbl.setFont(font)
        self.n_lbl.setStyleSheet("border: 2px solid white;\n"
"border-radius:20%;\n"
"color: white;")
        self.n_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Start = QtWidgets.QPushButton(self.frame_2)
        self.Start.setGeometry(QtCore.QRect(60, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(17)
        self.Start.setFont(font)
        self.Start.setStyleSheet("border-radius: 10px;\n"
"color: rgb(61,255,8);\n"
"background-color: rgb(20, 132,1);")
        self.Reset = QtWidgets.QPushButton(self.frame_2)
        self.Reset.setGeometry(QtCore.QRect(230, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(17)
        self.Reset.setFont(font)
        self.Reset.setStyleSheet("border-radius: 10px;\n"
"color: rgb(39,39,39);\n"
"background: grey;\n"
"")
        self.Reset.setEnabled(False)
        self.m_b = QtWidgets.QPushButton(self.frame_2)
        self.m_b.setGeometry(QtCore.QRect(30, 20, 25, 25))
        self.m_b.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_b.setIcon(icon)
        self.m_b.setIconSize(QtCore.QSize(25, 25))
        self.m_b.setStyleSheet("background: transparent;")
        self.e_b = QtWidgets.QPushButton(self.frame_2)
        self.e_b.setGeometry(QtCore.QRect(328, 20, 25, 25))
        self.e_b.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.e_b.setIcon(icon1)
        self.e_b.setIconSize(QtCore.QSize(25, 25))
        self.e_b.setStyleSheet("background:transparent")
        Form.setWindowTitle("Stopwatch")
        self.header.setText("Study Time")
        self.n_lbl.setText("00:00:00:00")
        self.Start.setText("Start")
        self.Reset.setText("Reset")
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Start.clicked.connect(self.StartF)
        self.Reset.clicked.connect(self.ResetF)
        self.m_b.clicked.connect(self.minimise)
        self.e_b.clicked.connect(self.Close)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.main)
        self.timer.start(10)
        self.flag = False
import gui_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
