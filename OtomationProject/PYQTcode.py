# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectA.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout
from PyQt5.QtCore import *
import pyfirmata
import time


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 980, 440))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: rgb(255, 170, 0);\n"
"\n"
"border-top-left-radius: 25px;\n"
"border-top-right-radius: 25px;\n"
"border-bottom-left-radius: 25px;\n"
"border-bottom-right-radius: 25px;\n"
"}")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 980, 100))
        self.frame.setStyleSheet("QFrame#frame{\n"
"border-image: url(:/imagenes/baner.png);\n"
"border-top-left-radius: 25px;\n"
"border-top-right-radius: 25px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 0, 571, 101))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 53 Ex")
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: blue;")
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(920, 0, 61, 31))
        self.exit.setStyleSheet("QPushButton#salir{\n"
"background-color: rgba(0,0,0,0);\n"
"color:white;\n"
"border-top-right-radius: 25px;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton#salir:hover{\n"
"background-color: rgb(255, 47, 47);\n"
"color:white;\n"
"border-top-right-radius: 25px;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton#salir:pressed{\n"
"background-color: rgb(206, 38, 38);\n"
"color:white;\n"
"border-top-right-radius: 25px;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.exit.setObjectName("exit")
        self.mini = QtWidgets.QPushButton(self.frame)
        self.mini.setGeometry(QtCore.QRect(860, 0, 61, 31))
        self.mini.setStyleSheet("QPushButton#mini{\n"
"background-color: rgba(0,0,0,0);\n"
"color:white;\n"
"    font: 24pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton#mini:hover{\n"
"background-color: rgba(0,0,0,40);\n"
"color:white;\n"
"    font: 24pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton#mini:pressed{\n"
"background-color: rgba(0,0,0,80);\n"
"color:white;\n"
"    font: 24pt \"MS Shell Dlg 2\";\n"
"}")
        self.mini.setObjectName("mini")
        self.label_led1 = QtWidgets.QLabel(self.widget)
        self.label_led1.setGeometry(QtCore.QRect(70, 100, 161, 71))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 53 Ex")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_led1.setFont(font)
        self.label_led1.setStyleSheet("\n"
"color: white;")
        self.label_led1.setObjectName("label_led1")
        self.label_gecit = QtWidgets.QLabel(self.widget)
        self.label_gecit.setGeometry(QtCore.QRect(380, 100, 191, 71))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 53 Ex")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_gecit.setFont(font)
        self.label_gecit.setStyleSheet("\n"
"color: white;")
        self.label_gecit.setObjectName("label_gecit")
        self.label_motorilerigeri = QtWidgets.QLabel(self.widget)
        self.label_motorilerigeri.setGeometry(QtCore.QRect(670, 100, 241, 71))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 53 Ex")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_motorilerigeri.setFont(font)
        self.label_motorilerigeri.setStyleSheet("\n"
"color: white;")
        self.label_motorilerigeri.setObjectName("label_motorilerigeri")
        self.label_led2 = QtWidgets.QLabel(self.widget)
        self.label_led2.setGeometry(QtCore.QRect(390, 260, 181, 71))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 53 Ex")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_led2.setFont(font)
        self.label_led2.setStyleSheet("\n"
"color: white;")
        self.label_led2.setObjectName("label_led2")
        self.led2_slider = QtWidgets.QSlider(self.widget)
        self.led2_slider.setGeometry(QtCore.QRect(430, 320, 91, 61))
        self.led2_slider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.led2_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid black;\n"
"height: 30px;\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(61, 61, 61);\n"
"    border: 1px solid black;\n"
"    width: 30px;\n"
"margin: 0px -1;\n"
"/*    margin: 2px 0;  handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
" border-radius: 15px;\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: rgb(230, 0, 0);\n"
"border: 2px solid black;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"background:rgb(0, 170, 0);\n"
"border: 2px solid black;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"}")
        self.led2_slider.setMaximum(1)
        self.led2_slider.setSingleStep(1)
        self.led2_slider.setPageStep(1)
        self.led2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.led2_slider.setObjectName("led2_slider")
        self.led1_on = QtWidgets.QPushButton(self.widget)
        self.led1_on.setGeometry(QtCore.QRect(70, 180, 81, 81))
        self.led1_on.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.led1_on.setStyleSheet("QPushButton#foco_on{\n"
"border-radius: 40px;\n"
"border: 3px solid black;\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton#foco_on:hover{\n"
"border-radius: 40px;\n"
"border: 3px solid black;\n"
"    background-color: rgb(67, 202, 99);\n"
"}\n"
"\n"
"QPushButton#foco_on:pressed{\n"
"border-radius: 40px;\n"
"border: 3px solid black;\n"
"    background-color: rgb(54, 162, 79);\n"
"}")
        self.led1_on.setObjectName("led1_on")
        self.led1_off = QtWidgets.QPushButton(self.widget)
        self.led1_off.setGeometry(QtCore.QRect(160, 180, 80, 80))
        self.led1_off.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.led1_off.setStyleSheet("QPushButton#foco_off{\n"
"border-radius: 40px;\n"
"border: 3px solid black;\n"
"    background-color: #ff5959;\n"
"}\n"
"\n"
"QPushButton#foco_off:hover{\n"
"border-radius: 40px;\n"
"border: 3px solid black;\n"
"    background-color: #d04848;\n"
"}\n"
"\n"
"QPushButton#foco_off:pressed{\n"
"border-radius: 40px;\n"
"border: 3px solid black;\n"
"    background-color: #aa3a3a;\n"
"}")
        self.led1_off.setObjectName("led1_off")
        self.gecit_open = QtWidgets.QPushButton(self.widget)
        self.gecit_open.setGeometry(QtCore.QRect(330, 180, 271, 31))
        self.gecit_open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gecit_open.setStyleSheet("QPushButton#puerta_open{\n"
"background-color: rgba(0,0,0,0);\n"
"border-radius: 15px;\n"
"border: 3px solid black;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}\n"
"\n"
"QPushButton#puerta_open:hover{\n"
"background-color: rgba(0,0,0,50);\n"
"border-radius: 15px;\n"
"color:white;\n"
"border: 3px solid white;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}\n"
"\n"
"QPushButton#puerta_open:pressed{\n"
"background-color: rgba(0,0,0,100);\n"
"border-radius: 15px;\n"
"color:white;\n"
"border: 3px solid white;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}")
        self.gecit_open.setObjectName("gecit_open")
        self.gecit_close = QtWidgets.QPushButton(self.widget)
        self.gecit_close.setGeometry(QtCore.QRect(330, 220, 271, 31))
        self.gecit_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gecit_close.setStyleSheet("QPushButton#puerta_close{\n"
"background-color: rgba(0,0,0,0);\n"
"border-radius: 15px;\n"
"border: 3px solid black;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}\n"
"\n"
"QPushButton#puerta_close:hover{\n"
"background-color: rgba(0,0,0,50);\n"
"border-radius: 15px;\n"
"color:white;\n"
"border: 3px solid white;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}\n"
"\n"
"QPushButton#puerta_close:pressed{\n"
"background-color: rgba(0,0,0,100);\n"
"border-radius: 15px;\n"
"color:white;\n"
"border: 3px solid white;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}")
        self.gecit_close.setObjectName("gecit_close")
        self.motor_ileri = QtWidgets.QPushButton(self.widget)
        self.motor_ileri.setGeometry(QtCore.QRect(650, 180, 271, 31))
        self.motor_ileri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.motor_ileri.setStyleSheet("QPushButton#ventana_open{\n"
"background-color: rgba(0,0,0,0);\n"
"border-radius: 15px;\n"
"border: 3px solid black;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}\n"
"\n"
"QPushButton#ventana_open:hover{\n"
"background-color: rgba(0,0,0,50);\n"
"border-radius: 15px;\n"
"color:white;\n"
"border: 3px solid white;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}\n"
"\n"
"QPushButton#ventana_open:pressed{\n"
"background-color: rgba(0,0,0,100);\n"
"border-radius: 15px;\n"
"color:white;\n"
"border: 3px solid white;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}")
        self.motor_ileri.setObjectName("motor_ileri")
        self.motor_geri = QtWidgets.QPushButton(self.widget)
        self.motor_geri.setGeometry(QtCore.QRect(650, 220, 271, 31))
        self.motor_geri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.motor_geri.setStyleSheet("QPushButton#ventana_close{\n"
"background-color: rgba(0,0,0,0);\n"
"border-radius: 15px;\n"
"border: 3px solid black;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}\n"
"\n"
"QPushButton#ventana_close:hover{\n"
"background-color: rgba(0,0,0,50);\n"
"border-radius: 15px;\n"
"color:white;\n"
"border: 3px solid white;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}\n"
"\n"
"QPushButton#ventana_close:pressed{\n"
"background-color: rgba(0,0,0,100);\n"
"border-radius: 15px;\n"
"color:white;\n"
"border: 3px solid white;\n"
"    font: 11pt \"Fixedsys\";\n"
"\n"
"}")
        self.motor_geri.setObjectName("motor_geri")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Otomasyon Projesi"))
        self.exit.setText(_translate("MainWindow", "X"))
        self.mini.setText(_translate("MainWindow", "-"))
        self.label_led1.setText(_translate("MainWindow", "    Led 1"))
        self.label_gecit.setText(_translate("MainWindow", "  Geçit"))
        self.label_motorilerigeri.setText(_translate("MainWindow", "Motor Yönü"))
        self.label_led2.setText(_translate("MainWindow", "    Led 2"))
        self.led1_on.setText(_translate("MainWindow", "Yan"))
        self.led1_off.setText(_translate("MainWindow", "Sön"))
        self.gecit_open.setText(_translate("MainWindow", "Açık"))
        self.gecit_close.setText(_translate("MainWindow", "Kapalı"))
        self.motor_ileri.setText(_translate("MainWindow", "İleri"))
        self.motor_geri.setText(_translate("MainWindow", "Geri"))

board = pyfirmata.Arduino('COM4')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
led1 = board.get_pin('d:4:o')
led2 = board.get_pin('d:9:o')
motor_der = board.get_pin('d:5:p')
motor_izq = board.get_pin('d:6:p')
servo = board.get_pin('d:7:s')
servo.write(180)

class WelcomeScreen(QMainWindow):


    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("projectA.ui", self)
        self.led1_on.clicked.connect(self.led1_ac)
        self.led1_off.clicked.connect(self.led1_kapa)

        self.gecit_open.clicked.connect(self.gecit_ac)
        self.gecit_close.clicked.connect(self.gecit_kapa)
        self.motor_ileri.clicked.connect(self.donus_1)
        self.motor_geri.clicked.connect(self.donus_2)
        self.led2_slider.valueChanged.connect(self.led2)
        self.frame.mouseMoveEvent = self.moveWindow
        self.exit.clicked.connect(self.pencere_kapa)
        self.mini.clicked.connect(self.kucult)

    def donus_1(self):
        motor_der.write(0.2)
        time.sleep(5)
        motor_der.write(0)

    def donus_2(self):
        motor_izq.write(0.2)
        time.sleep(5)
        motor_izq.write(0)

    def gecit_ac(self):
        servo.write(90)
        print("açık")

    def gecit_kapa(self):
        servo.write(180)
        print("kapalı")

    def led1_ac(self):
        led1.write(1)
        print("yandı")

    def led1_kapa(self):
        led1.write(0)
        print("söndü")

    def led2(self):
        data = int(self.led2_slider.value())
        led2.write(data)

    def pencere_kapa(self):
        app.exit()
        sys.exit()

    def kucult(self):
        widget.showMinimized()

    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()



# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(768)
widget.setFixedWidth(1366)
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Saliendo")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

