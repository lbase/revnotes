# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showtablewin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TblWin(object):
    def setupUi(self, TblWin):
        TblWin.setObjectName("TblWin")
        TblWin.resize(898, 646)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(TblWin.sizePolicy().hasHeightForWidth())
        TblWin.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(TblWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tb1 = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb1.sizePolicy().hasHeightForWidth())
        self.tb1.setSizePolicy(sizePolicy)
        self.tb1.setMinimumSize(QtCore.QSize(100, 0))
        self.tb1.setLineWidth(2)
        self.tb1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb1.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tb1.setObjectName("tb1")
        self.gridLayout.addWidget(self.tb1, 0, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btnRefresh = QtWidgets.QPushButton(self.splitter)
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnVform = QtWidgets.QPushButton(self.splitter)
        self.btnVform.setObjectName("btnVform")
        self.btnDelete = QtWidgets.QPushButton(self.splitter)
        self.btnDelete.setObjectName("btnDelete")
        self.btnCopy = QtWidgets.QPushButton(self.splitter)
        self.btnCopy.setObjectName("btnCopy")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.lineSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSearch.setObjectName("lineSearch")
        self.gridLayout.addWidget(self.lineSearch, 1, 1, 1, 1)
        TblWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TblWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 34))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        TblWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TblWin)
        self.statusbar.setObjectName("statusbar")
        TblWin.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(TblWin)
        self.toolBar.setObjectName("toolBar")
        TblWin.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtWidgets.QAction(TblWin)
        self.actionExit.setObjectName("actionExit")
        self.menu_File.addAction(self.actionExit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(TblWin)
        QtCore.QMetaObject.connectSlotsByName(TblWin)

    def retranslateUi(self, TblWin):
        _translate = QtCore.QCoreApplication.translate
        TblWin.setWindowTitle(_translate("TblWin", "Review Notes"))
        self.btnRefresh.setText(_translate("TblWin", "Refresh"))
        self.btnVform.setText(_translate("TblWin", "Add &New"))
        self.btnDelete.setText(_translate("TblWin", "Delete"))
        self.btnCopy.setText(_translate("TblWin", "Co&py"))
        self.menu_File.setTitle(_translate("TblWin", "&File"))
        self.toolBar.setWindowTitle(_translate("TblWin", "toolBar"))
        self.actionExit.setText(_translate("TblWin", "Exit"))
