# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HospitalUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 150, 931, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 80, 141, 21))
        self.label.setStyleSheet("font: 14pt \"Algerian\";")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(790, 60, 111, 51))
        self.pushButton_5.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 70, 251, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 460, 171, 81))
        self.pushButton_4.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 460, 181, 81))
        self.pushButton_2.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 460, 171, 81))
        self.pushButton_3.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 50, 171, 71))
        self.pushButton.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 570, 191, 81))
        self.pushButton_6.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(580, 570, 201, 81))
        self.pushButton_7.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(self.lineEdit.clear) # type: ignore
        self.pushButton_5.clicked.connect(self.tableWidget.clearContents) # type: ignore
        self.pushButton_2.clicked.connect(MainWindow.slot1) # type: ignore
        self.pushButton_3.clicked.connect(MainWindow.slot2) # type: ignore
        self.pushButton_4.clicked.connect(MainWindow.slot3) # type: ignore
        self.pushButton_6.clicked.connect(MainWindow.slot4) # type: ignore
        self.pushButton_7.clicked.connect(MainWindow.slot5) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "医院主界面（查询预约和接种信息）"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2."))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3."))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4."))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5."))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6."))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7."))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8."))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9."))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "信息编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "预约人ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "接种单位编号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "疫苗编号"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "接种剂次"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "预约日期"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "接种时间"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "完成情况"))
        self.label.setText(_translate("MainWindow", "请输入本院ID"))
        self.pushButton_5.setText(_translate("MainWindow", "刷新"))
        self.pushButton_4.setText(_translate("MainWindow", "查询疫苗入库信息"))
        self.pushButton_2.setText(_translate("MainWindow", "处理接种预约"))
        self.pushButton_3.setText(_translate("MainWindow", "查询仓库信息"))
        self.pushButton.setText(_translate("MainWindow", "查询预约接种信息"))
        self.pushButton_6.setText(_translate("MainWindow", "查询疫苗订购信息"))
        self.pushButton_7.setText(_translate("MainWindow", "购买疫苗"))
