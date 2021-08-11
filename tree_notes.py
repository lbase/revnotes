# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_notes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TreeNotesWin(object):
    def setupUi(self, TreeNotesWin):
        TreeNotesWin.setObjectName("TreeNotesWin")
        TreeNotesWin.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/pipette"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TreeNotesWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TreeNotesWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lblLineEdit = QtWidgets.QLabel(self.centralwidget)
        self.lblLineEdit.setObjectName("lblLineEdit")
        self.gridLayout.addWidget(self.lblLineEdit, 0, 0, 1, 1)
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout.addWidget(self.searchEdit, 0, 1, 1, 2)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout.addWidget(self.btnSearch, 0, 3, 1, 1)
        self.treeRevNote = QtWidgets.QTreeView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(25)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeRevNote.sizePolicy().hasHeightForWidth())
        self.treeRevNote.setSizePolicy(sizePolicy)
        self.treeRevNote.setMinimumSize(QtCore.QSize(40, 0))
        self.treeRevNote.setObjectName("treeRevNote")
        self.gridLayout.addWidget(self.treeRevNote, 1, 0, 1, 2)
        self.txtRevNote = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(75)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtRevNote.sizePolicy().hasHeightForWidth())
        self.txtRevNote.setSizePolicy(sizePolicy)
        self.txtRevNote.setMinimumSize(QtCore.QSize(75, 0))
        self.txtRevNote.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.txtRevNote.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtRevNote.setObjectName("txtRevNote")
        self.gridLayout.addWidget(self.txtRevNote, 1, 2, 1, 2)
        TreeNotesWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TreeNotesWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 34))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        TreeNotesWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TreeNotesWin)
        self.statusbar.setObjectName("statusbar")
        TreeNotesWin.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(TreeNotesWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        TreeNotesWin.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Open = QtWidgets.QAction(TreeNotesWin)
        self.action_Open.setObjectName("action_Open")
        self.action_New = QtWidgets.QAction(TreeNotesWin)
        self.action_New.setObjectName("action_New")
        self.actionRename = QtWidgets.QAction(TreeNotesWin)
        self.actionRename.setObjectName("actionRename")
        self.action = QtWidgets.QAction(TreeNotesWin)
        self.action.setObjectName("action")
        self.actionReName = QtWidgets.QAction(TreeNotesWin)
        self.actionReName.setObjectName("actionReName")
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.action_New)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionReName)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBar.addSeparator()

        self.retranslateUi(TreeNotesWin)
        QtCore.QMetaObject.connectSlotsByName(TreeNotesWin)

    def retranslateUi(self, TreeNotesWin):
        _translate = QtCore.QCoreApplication.translate
        TreeNotesWin.setWindowTitle(_translate("TreeNotesWin", "MainWindow"))
        self.lblLineEdit.setText(_translate("TreeNotesWin", "<html><head/><body><p>Search</p></body></html>"))
        self.btnSearch.setText(_translate("TreeNotesWin", "Search"))
        self.menuFile.setTitle(_translate("TreeNotesWin", "File"))
        self.menuEdit.setTitle(_translate("TreeNotesWin", "Edit"))
        self.toolBar.setWindowTitle(_translate("TreeNotesWin", "toolBar"))
        self.action_Open.setText(_translate("TreeNotesWin", "&Open"))
        self.action_New.setText(_translate("TreeNotesWin", "&New"))
        self.actionRename.setText(_translate("TreeNotesWin", "Rename"))
        self.action.setText(_translate("TreeNotesWin", "Rename"))
        self.actionReName.setText(_translate("TreeNotesWin", "ReName"))
import tbar_rc
