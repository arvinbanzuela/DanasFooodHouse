# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import  *
import pymysql.cursors
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot



class DanasMainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'DANAS-INVENTORY'
        self.initUI()

    def initUI(self):
        # Creation of Main Interface of System - Tab Widget

        DanasMainWin.resize(818, 567)
        self.centralwidget = QWidget(DanasMainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 551))
        self.tabWidget.setObjectName("tabWidget")

        # ============= Dashboard Tab Layout =========================

        self.Dashboard = QtWidgets.QWidget()
        self.Dashboard.setObjectName("Dashboard")
        self.calendarDanas = QtWidgets.QCalendarWidget(self.Dashboard)
        self.calendarDanas.setGeometry(QtCore.QRect(20, 140, 341, 251))
        self.calendarDanas.setObjectName("calendarDanas")
        self.userGroup = QtWidgets.QGroupBox(self.Dashboard)
        self.userGroup.setGeometry(QtCore.QRect(20, 10, 341, 111))
        self.userGroup.setObjectName("userGroup")
        self.groupBox_4 = QtWidgets.QGroupBox(self.userGroup)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 190, 411, 301))
        self.groupBox_4.setObjectName("groupBox_4")
        self.recentActivityGroup = QtWidgets.QGroupBox(self.Dashboard)
        self.recentActivityGroup.setGeometry(QtCore.QRect(380, 10, 391, 501))
        self.recentActivityGroup.setObjectName("recentActivityGroup")
        self.tabWidget.addTab(self.Dashboard, "")

        # ================= Inventory Tab Layout =======================
        self.Inventory = QtWidgets.QWidget()
        self.Inventory.setObjectName("Inventory")
        self.tableInventoryView = QtWidgets.QTableView(self.Inventory)
        self.tableInventoryView.setGeometry(QtCore.QRect(20, 80, 761, 431))
        self.tableInventoryView.setShowGrid(False)
        self.tableInventoryView.setObjectName("tableInventoryView")
        self.searchBarInventory = QtWidgets.QLineEdit(self.Inventory)
        self.searchBarInventory.setGeometry(QtCore.QRect(20, 20, 581, 41))
        self.searchBarInventory.setObjectName("searchBarInventory")
        self.SearchButtonInventory = QtWidgets.QPushButton(self.Inventory)
        self.SearchButtonInventory.setGeometry(QtCore.QRect(620, 20, 41, 41))
        self.SearchButtonInventory.setObjectName("SearchButtonInventory")
        self.AddButtonInventory = QtWidgets.QPushButton(self.Inventory)
        self.AddButtonInventory.setGeometry(QtCore.QRect(680, 20, 41, 41))
        self.AddButtonInventory.setObjectName("AddButtonInventory")
        self.DeleteButtonInventory = QtWidgets.QPushButton(self.Inventory)
        self.DeleteButtonInventory.setGeometry(QtCore.QRect(740, 20, 41, 41))
        self.DeleteButtonInventory.setObjectName("DeleteButtonInventory")
        self.tabWidget.addTab(self.Inventory, "")

        # ======================= Orders Tab Layout ===================

        self.Orders = QtWidgets.QWidget()
        self.Orders.setObjectName("Orders")
        self.TotalAmountDisplay = QtWidgets.QLCDNumber(self.Orders)
        self.TotalAmountDisplay.setGeometry(QtCore.QRect(180, 450, 161, 61))
        self.TotalAmountDisplay.setObjectName("TotalAmountDisplay")
        self.Menu = QtWidgets.QGroupBox(self.Orders)
        self.Menu.setGeometry(QtCore.QRect(360, 60, 431, 121))
        self.Menu.setObjectName("Menu")
        self.BurgersButton = QtWidgets.QPushButton(self.Menu)
        self.BurgersButton.setGeometry(QtCore.QRect(10, 20, 151, 51))
        self.BurgersButton.setObjectName("BurgersButton")
        self.PastaButton = QtWidgets.QPushButton(self.Menu)
        self.PastaButton.setGeometry(QtCore.QRect(160, 20, 131, 51))
        self.PastaButton.setObjectName("PastaButton")
        self.MealsButton = QtWidgets.QPushButton(self.Menu)
        self.MealsButton.setGeometry(QtCore.QRect(290, 20, 131, 51))
        self.MealsButton.setObjectName("MealsButton")
        self.SpecialSilogButton = QtWidgets.QPushButton(self.Menu)
        self.SpecialSilogButton.setGeometry(QtCore.QRect(10, 70, 201, 41))
        self.SpecialSilogButton.setObjectName("SpecialSilogButton")
        self.DrinksButton = QtWidgets.QPushButton(self.Menu)
        self.DrinksButton.setGeometry(QtCore.QRect(210, 70, 211, 41))
        self.DrinksButton.setObjectName("DrinksButton")
        self.OrdersMenuChoices = QtWidgets.QGroupBox(self.Orders)
        self.OrdersMenuChoices.setGeometry(QtCore.QRect(360, 190, 431, 331))
        self.OrdersMenuChoices.setObjectName("OrdersMenuChoices")
        self.OrdersSearchBar = QtWidgets.QLineEdit(self.Orders)
        self.OrdersSearchBar.setGeometry(QtCore.QRect(360, 10, 381, 41))
        self.OrdersSearchBar.setObjectName("OrdersSearchBar")
        self.OrdersTableView = QtWidgets.QTableView(self.Orders)
        self.OrdersTableView.setGeometry(QtCore.QRect(10, 60, 341, 331))
        self.OrdersTableView.setObjectName("OrdersTableView")
        self.OrdersSearchBarButton = QtWidgets.QPushButton(self.Orders)
        self.OrdersSearchBarButton.setGeometry(QtCore.QRect(750, 10, 41, 41))
        self.OrdersSearchBarButton.setObjectName("OrdersSearchBarButton")
        self.TotalAmount = QtWidgets.QLabel(self.Orders)
        self.TotalAmount.setGeometry(QtCore.QRect(16, 452, 151, 51))
        self.TotalAmount.setObjectName("TotalAmount")
        self.ProceedOrderButton = QtWidgets.QPushButton(self.Orders)
        self.ProceedOrderButton.setGeometry(QtCore.QRect(180, 410, 75, 23))
        self.ProceedOrderButton.setObjectName("ProceedOrderButton")
        self.CancelOrderButton = QtWidgets.QPushButton(self.Orders)
        self.CancelOrderButton.setGeometry(QtCore.QRect(270, 410, 75, 23))
        self.CancelOrderButton.setObjectName("CancelOrderButton")
        self.tabWidget.addTab(self.Orders, "")
        self.Reports = QtWidgets.QWidget()
        self.Reports.setObjectName("Reports")
        self.ReportsSearchBar = QtWidgets.QLineEdit(self.Reports)
        self.ReportsSearchBar.setGeometry(QtCore.QRect(20, 10, 601, 41))
        self.ReportsSearchBar.setObjectName("ReportsSearchBar")
        self.listView = QtWidgets.QListView(self.Reports)
        self.listView.setGeometry(QtCore.QRect(20, 100, 771, 391))
        self.listView.setObjectName("listView")
        self.ReportsSearchBarButton = QtWidgets.QPushButton(self.Reports)
        self.ReportsSearchBarButton.setGeometry(QtCore.QRect(640, 10, 41, 41))
        self.ReportsSearchBarButton.setObjectName("ReportsSearchBarButton")
        self.ReportsDownloadButton = QtWidgets.QPushButton(self.Reports)
        self.ReportsDownloadButton.setGeometry(QtCore.QRect(740, 10, 41, 41))
        self.ReportsDownloadButton.setObjectName("ReportsDownloadButton")
        self.ReportsViewButton = QtWidgets.QPushButton(self.Reports)
        self.ReportsViewButton.setGeometry(QtCore.QRect(690, 10, 41, 41))
        self.ReportsViewButton.setObjectName("ReportsViewButton")
        self.tabWidget.addTab(self.Reports, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userGroup.setTitle(_translate("MainWindow", "Welcome"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.recentActivityGroup.setTitle(_translate("MainWindow", "Recent Activity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dashboard), _translate("MainWindow", "Dashboard"))
        self.SearchButtonInventory.setText(_translate("MainWindow", "Search"))
        self.AddButtonInventory.setText(_translate("MainWindow", "Add"))
        self.DeleteButtonInventory.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inventory), _translate("MainWindow", "Inventory"))
        self.Menu.setTitle(_translate("MainWindow", "Menu"))
        self.BurgersButton.setText(_translate("MainWindow", "Burgers"))
        self.PastaButton.setText(_translate("MainWindow", "Pasta"))
        self.MealsButton.setText(_translate("MainWindow", "Meals"))
        self.SpecialSilogButton.setText(_translate("MainWindow", "Special Silog"))
        self.DrinksButton.setText(_translate("MainWindow", "Drinks"))
        self.OrdersMenuChoices.setTitle(_translate("MainWindow", "Orders"))
        self.OrdersSearchBarButton.setText(_translate("MainWindow", "Search"))
        self.TotalAmount.setText(_translate("MainWindow", "Total"))
        self.ProceedOrderButton.setText(_translate("MainWindow", "Proceed"))
        self.CancelOrderButton.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Orders), _translate("MainWindow", "Orders"))
        self.ReportsSearchBarButton.setText(_translate("MainWindow", "Search"))
        self.ReportsDownloadButton.setText(_translate("MainWindow", "Download"))
        self.ReportsViewButton.setText(_translate("MainWindow", "View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Reports), _translate("MainWindow", "Reports"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
