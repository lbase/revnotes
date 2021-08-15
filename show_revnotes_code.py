import sys
import os
from PyQt5.QtCore import QSize, QSortFilterProxyModel, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QDataWidgetMapper, QMainWindow, QTableView
from PyQt5 import QtCore
from PyQt5.QtGui import *
from icecream import ic
from show_revnotes import Ui_RevNoteWin


class Main(QMainWindow, Ui_RevNoteWin):
    def __init__(self, table_name="revnotes"):
        super().__init__()
        self.table_name = table_name
        self.ui = Ui_RevNoteWin()
        self.ui.setupUi(self)
        self.clipboard = QGuiApplication.clipboard()
        self.conn_name = "dbshowqry"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.db.setDatabaseName("/home/rfile/python3/revnotes/notes.db")
        ok = self.db.open()

        self.model = QSqlTableModel(db=self.db)
        self.addmap()

        self.model.setTable(self.table_name)
        self.model.select()
        self.mapper.toLast()

        self.ui.btnVform.clicked.connect(self.add_new)
        self.ui.btnRefresh.clicked.connect(self.refreshrecs)
        self.ui.actionExit.triggered.connect(self.exitFunc)
        self.ui.btnPrev.clicked.connect(self.mapper.toPrevious)
        self.ui.btnNext.clicked.connect(self.mapper.toNext)
        self.ui.btnCopy.clicked.connect(self.txt_to_clp)
        self.ui.lineSearch.returnPressed.connect(self.filterTable)
        # self.ui.lineSearch.keyPressEvent.connect()
        # self.ui.btnGraphbp.clicked.connect(self.bpgraph)
        self.ui.btnDelete.clicked.connect(self.delrows)

        self.setWindowTitle(table_name)

    def addmap(self):
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.ui.spinID, 0)
        self.mapper.addMapping(self.ui.spinCat, 1)
        self.mapper.addMapping(self.ui.txtTitle, 2)
        self.mapper.addMapping(self.ui.txtContent, 3)

        # self.mapper.submit()
        # self.model.select()

        ic(self.mapper.submit())

        # self.showSbar("Setup Complete")
        # proxy
    def lclproxy(self):
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(-1)  # Search all columns.
        self.proxy_model.setSourceModel(self.model)

        self.proxy_model.sort(0, Qt.AscendingOrder)
        self.mapper.setModel(self.proxy_model)
        self.ui.lineSearch.textChanged.connect(
            self.proxy_model.setFilterFixedString)

    def add_new(self):
        self.model.insertRow(0)

    def refreshrecs(self):
        self.model.setFilter('')
        self.model.select()
        self.mapper.submit()
        # self.ui.tb1.setModel(self.model)
        #self.ui.tb1.reset()
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
        self.ui.txtContent.setModel(self.proxy_model)
        self.ui.txtContent.reset()
        search = QtCore.QRegExp(self.text, QtCore.Qt.CaseInsensitive,
                                QtCore.QRegExp.RegExp)
        self.proxy_model.setFilterRegExp(search)

        self.proxy.setFilterRegExp(search)

    def showSbar(self, msg):
        self.ui.statusbar.showMessage(msg)

    def txt_to_clp(self):
        self.cursor = self.ui.txtContent.textCursor()
        ic("Selection start: %d end: %d" %
           (self.cursor.selectionStart(), self.cursor.selectionEnd()))
        ic(self.cursor.selectedText())
        self.clipboard.setText(self.ui.txtContent.toPlainText())

    def filterTable(self):
        self.filterText = self.ui.lineSearch.text()
        self.filterQuery = 'content like %' + self.filterText + '%'
        self.model.setFilter(self.filterQuery)
        self.model.select()
        self.mapper.submit()
        # self.ui.tb1.setModel(self.model)

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

    def exitFunc(self):
        self.db.close()
        ic(self.model.lastError().text())
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # clipboard = app.clipboard()

    main = Main()
    # main.addmap()
    main.show()
    sys.exit(app.exec_())
