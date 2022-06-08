# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'det_calc_app4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QtCore.QSize(300, 500))
        MainWindow.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Program_name = QtWidgets.QLabel(self.centralwidget)
        self.Program_name.setGeometry(QtCore.QRect(0, 40, 301, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Program_name.setFont(font)
        self.Program_name.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(255, 255, 0);\n"
"border-color: rgb(255, 17, 88);")
        self.Program_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Program_name.setObjectName("Program_name")
        self.A21 = QtWidgets.QTextEdit(self.centralwidget)
        self.A21.setGeometry(QtCore.QRect(85, 210, 30, 30))
        self.A21.setOverwriteMode(True)
        self.A21.setObjectName("A21")
        self.A11 = QtWidgets.QTextEdit(self.centralwidget)
        self.A11.setGeometry(QtCore.QRect(85, 170, 30, 30))
        self.A11.setOverwriteMode(True)
        self.A11.setObjectName("A11")
        self.A31 = QtWidgets.QTextEdit(self.centralwidget)
        self.A31.setGeometry(QtCore.QRect(85, 250, 30, 30))
        self.A31.setOverwriteMode(True)
        self.A31.setObjectName("A31")
        self.A12 = QtWidgets.QTextEdit(self.centralwidget)
        self.A12.setGeometry(QtCore.QRect(125, 170, 30, 30))
        self.A12.setOverwriteMode(True)
        self.A12.setObjectName("A12")
        self.A22 = QtWidgets.QTextEdit(self.centralwidget)
        self.A22.setGeometry(QtCore.QRect(125, 210, 30, 30))
        self.A22.setOverwriteMode(True)
        self.A22.setObjectName("A22")
        self.A32 = QtWidgets.QTextEdit(self.centralwidget)
        self.A32.setGeometry(QtCore.QRect(125, 250, 30, 30))
        self.A32.setOverwriteMode(True)
        self.A32.setObjectName("A32")
        self.A13 = QtWidgets.QTextEdit(self.centralwidget)
        self.A13.setGeometry(QtCore.QRect(165, 170, 30, 30))
        self.A13.setOverwriteMode(True)
        self.A13.setObjectName("A13")
        self.A23 = QtWidgets.QTextEdit(self.centralwidget)
        self.A23.setGeometry(QtCore.QRect(165, 210, 30, 30))
        self.A23.setOverwriteMode(True)
        self.A23.setObjectName("A23")
        self.A33 = QtWidgets.QTextEdit(self.centralwidget)
        self.A33.setGeometry(QtCore.QRect(165, 250, 30, 30))
        self.A33.setOverwriteMode(True)
        self.A33.setObjectName("A33")
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(85, 290, 110, 21))
        self.Calculate.setStyleSheet("background-color: rgb(173, 106, 255);")
        self.Calculate.setObjectName("Calculate")
        self.Answer = QtWidgets.QLabel(self.centralwidget)
        self.Answer.setGeometry(QtCore.QRect(85, 360, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Answer.setFont(font)
        self.Answer.setText("")
        self.Answer.setAlignment(QtCore.Qt.AlignCenter)
        self.Answer.setObjectName("Answer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_funcs()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Program_name.setText(_translate("MainWindow", "Определитель 3х3"))
        self.Calculate.setText(_translate("MainWindow", "Посчитать"))

    def det_3(self):
        if self.A11.toPlainText() != '':
            a11 = int(self.A11.toPlainText())
            a12 = int(self.A12.toPlainText())
            a13 = int(self.A13.toPlainText())
            a21 = int(self.A21.toPlainText())
            a22 = int(self.A22.toPlainText())
            a23 = int(self.A23.toPlainText())
            a31 = int(self.A31.toPlainText())
            a32 = int(self.A32.toPlainText())
            a33 = int(self.A33.toPlainText())
            self.Answer.setText(str(a11 * a22 * a33 + a12 * a23 * a31 + a21 * a32 * a13 - a13 * a22 * a31 - a11 * a23 * a32 - a33 * a12 * a21))


    def add_funcs(self):
        self.Calculate.clicked.connect(lambda: self.det_3())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())