import sys
import os
from PyQt5.QtCore import QSize, QSortFilterProxyModel, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5 import QtCore
from PyQt5.QtGui import *
from icecream import ic
from showtablewin import Ui_TblWin


class Main(QMainWindow, Ui_TblWin):
    def __init__(self, table_name="revnotes"):
        super().__init__()
        self.ui = Ui_TblWin()
        self.ui.setupUi(self)
        self.clipboard = QGuiApplication.clipboard()
        self.conn_name = "dbshowqry"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.db.setDatabaseName("/home/rfile/python3/revnotes/notes.db")
        ok = self.db.open()
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable(table_name)
        self.ui.tb1.setModel(self.model)
        # self.model.setSort(0, Qt.DescendingOrder)
        # self.model.setFilter("content like '%cache%'")
        self.model.select()

        # proxy
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(
            3)  # Search all columns is -1 3 should be content
        self.proxy_model.setSourceModel(self.model)
        # self.proxy_model.dynamicSortFilter()
        self.proxy_model.sort(0, Qt.AscendingOrder)

        self.ui.tb1.setModel(self.proxy_model)

        self.ui.tb1.setModel(self.proxy_model)
        # self.ui.tb1.resizeRowsToContents()
        #self.ui.tb1.resizeColumnsToContents()

        # self.ui.tb1.setColumnWidth(2, 200)
        # self.ui.tb1.setColumnWidth(3, 500)
        self.ui.tb1.resizeColumnToContents(3)
        #self.ui.tb1.resizeRowsToContents()
        self.ui.tb1.setColumnHidden(0, 1)
        self.ui.tb1.setColumnHidden(1, 1)
        self.ui.tb1.setColumnHidden(2, 1)
        # self.ui.tb1.setColumnWidth(3, 300)
        #self.ui.tb1.setRowHeight(100)
        # self.ui.tb1.setSelectionBehavior(0)
        # self.ui.tb1.clicked.connect(self.copy_Content)
        # self.ui.tb1.wordWrap()
        self.ui.btnVform.clicked.connect(self.add_new)
        self.ui.btnRefresh.clicked.connect(self.refreshrecs)
        self.ui.actionExit.triggered.connect(self.exitFunc)
        # self.ui.btnGraphbp.clicked.connect(self.bpgraph)
        self.ui.btnDelete.clicked.connect(self.delrows)
        # self.ui.btnCopy.clicked.connect(self.copy_cell)
        self.ui.tb1.clicked.connect(self.cell_was_clicked)

        self.setWindowTitle(table_name)
        # self.ui.lineSearch.textChanged.connect(
        # self.ui.lineSearch.textEdited.connect(
        #    self.proxy_model.setFilterFixedString)
        #self.ui.lineSearch.returnPressed.connect(self.proxyFilterTable)
        #self.ui.lineSearch.textChanged.connect(
        #    self.proxy_model.setFilterFixedString)
        self.ui.lineSearch.textChanged.connect(
            self.proxy_model.setFilterRegExp)

        self.showSbar("Setup Complete")

    def add_new(self):
        self.model.insertRow(0)

    def refreshrecs(self):
        self.model.setFilter('')
        self.model.select()
        # self.ui.tb1.setModel(self.model)
        self.ui.tb1.reset()
        self.showSbar("refresh")

    def filterTable(self):
        self.filterText = self.ui.lineSearch.text()
        self.filterQuery = 'content like %' + self.filterText + '%'
        self.model.setFilter(self.filterQuery)
        self.model.select()
        # self.ui.tb1.setModel(self.model)
        self.ui.tb1.reset()

    @QtCore.pyqtSlot(str)
    def proxyFilterTable(self):
        self.text = self.ui.lineSearch.text()
        #self.filterText = self.ui.lineSearch.text()
        #self.filterQuery = 'content like %' + self.filterText + '%'
        #self.proxy_model.setFilter(self.filterQuery)

        self.proxy_model.select()
        self.ui.tb1.setModel(self.proxy_model)
        self.ui.tb1.reset()
        search = QtCore.QRegExp(self.text, QtCore.Qt.CaseInsensitive,
                                QtCore.QRegExp.RegExp)
        self.proxy_model.setFilterRegExp(search)

        self.proxy.setFilterRegExp(search)

    def showSbar(self, msg):
        self.ui.statusbar.showMessage(msg)

    def delrows(self):
        self.showSbar("remove highlighted rows")
        l = self.ui.tb1.selectedIndexes()
        if not len(l):
            return
        else:
            self.showSbar(str(len(l) / 8) + " rows selected")
        rows = set([i.row() for i in l])
        rows = list(rows)
        rows.sort()
        first = rows[0]
        count = len(rows)
        self.model.removeRows(first, count)
        self.model.submitAll()

    def copy_cell(self):
        # self.col = self.ui.tb1.selectedIndexes()
        self.sel_index = (self.ui.tb1.selectionModel().currentIndex())
        self.sel_value = self.sel_index.sibling(
            self.sel_index.row(), self.sel_index.column()).data()
        ic(self.sel_value)
        self.clipboard.setText(self.sel_value)

    def cell_was_clicked(self):
        # row = self.ui.tb1.rowAt()
        # column = self.ui.tb1.columnAt()
        # print("Row %d and Column %d was clicked" % (row, column))
        # item = self.ui.tb1.itemAt(row, column)
        # self.ID = item.text()
        # ic(self.ID)
        # #selected cell value.
        self.sel_index = (self.ui.tb1.selectionModel().currentIndex())
        # print(index)
        self.sel_value = self.sel_index.sibling(
            self.sel_index.row(), self.sel_index.column()).data()
        self.clipboard.setText(self.sel_value)
        # ic(self.sel_value)

    def exitFunc(self):
        self.db.close()
        ic(self.model.lastError().text())
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # clipboard = app.clipboard()

    main = Main()
    main.show()
    sys.exit(app.exec_())
