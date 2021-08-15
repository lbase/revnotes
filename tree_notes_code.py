import sys, os
from PyQt5 import QtGui
from icecream import ic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir, QFile
# from PyQt5.QtGui import QClipboard, QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtGui import *
from tree_notes import Ui_TreeNotesWin
import tbar_rc
from lclsearch import revsearch, TableModel
# tablemodel

from PyQt5.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel

ic.disable()


class Main(QtWidgets.QMainWindow, Ui_TreeNotesWin):
    """docstring for main."""
    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_TreeNotesWin()
        self.ui.setupUi(self)
        self.setuptreeview()
        self.setuptbar()
        self.clipboard = QGuiApplication.clipboard()

    def setuptreeview(self):
        self.dir = revsearch.TxtFileList(self, "/home/rfile/revclips/")
        ic(self.dir)
        self.lst = revsearch.TxtFiles(self, "/home/rfile/revclips")
        ic(self.lst)
        self.txtbody = revsearch.TxtFileBody(self,
                                             "/home/rfile/revclips/*.txt")
        #ic(self.txtbody)
        self.treemodel = QStandardItemModel(0, 1)

        #self.ui.treeRevNote.resizeColumnToContents(0)
        # self.ui.treeRevNote.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        self.ui.treeRevNote.setModel(self.treemodel)
        for y in (self.lst):
            self.myitem = y
            self.treemodel.appendRow(QStandardItem(self.myitem))
        self.ui.treeRevNote.clicked.connect(self.get_Val_edit)

    def setuptbar(self):
        self.tbarbtn01 = QtWidgets.QAction("open", self)
        self.tbarbtn01.setIcon(QIcon(":/icons/bdoccopy.png"))
        self.tbarbtn01.setStatusTip("open")
        self.tbarbtn01.triggered.connect(self.get_Val_tbar_edit)
        self.ui.toolBar.addAction(self.tbarbtn01)
        self.tbarbtn02 = QtWidgets.QAction("copy_all", self)
        self.tbarbtn02.setStatusTip("copy all")
        self.tbarbtn02.setIcon(QIcon(":/icons/cliptext.png"))
        self.tbarbtn02.triggered.connect(self.txt_to_clp)
        self.ui.toolBar.addAction(self.tbarbtn02)
        self.tbarbtn03 = QtWidgets.QAction("rename", self)
        self.tbarbtn03.setStatusTip("rename file")
        self.tbarbtn03.setIcon(QIcon(":icons/docrename.png"))
        self.tbarbtn03.triggered.connect(self.file_rename)
        self.ui.toolBar.addAction(self.tbarbtn03)
        self.tbarbtn04 = QtWidgets.QAction('copy sel', self)
        self.tbarbtn04.setIcon(QIcon(":/icons/clippast.png"))
        self.tbarbtn04.setStatusTip("copy selection")
        self.tbarbtn04.triggered.connect(self.sel_txt_to_clp)
        self.ui.toolBar.addAction(self.tbarbtn04)
        #menu file rename
        self.ui.actionReName.triggered.connect(self.file_rename)
        self.setupModel()
        #self.ui.toolBar
        self.ui.btnSearch.clicked.connect(self.file_search)
        self.ui.btnNext.setEnabled(False)
        self.ui.searchEdit.returnPressed.connect(self.file_search)
        self.ui.searchEdit.textChanged.connect(
            self.proxy_model.setFilterFixedString)

    def setupModel(self):
        self.model = TableModel(self.txtbody)
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        self.proxy_model.setFilterKeyColumn(-1)  # Search all columns.
        self.proxy_model.sort(0, Qt.AscendingOrder)

        self.ui.txtRevNote.setModel(self.proxy_model)

    def get_Val_edit(self, val):
        self.idx = val.row()
        self.txt = self.dir[self.idx]
        ic(val.data())
        ic(val.row())
        ic(self.txt)
        self.myfname = self.dir[self.idx]
        ic(self.myfname)
        self.ui.txtRevNote.setText(self.txtbody[val.row()])

    def get_Val_tbar_edit(self):
        self.highlightindex = self.ui.treeRevNote.selectedIndexes()
        ic(self.highlightindex)
        self.myfname = self.dir[self.highlightindex]
        ic(self.myfname)
        self.fod = open(self.myfname)
        self.fdata = self.fod.read()
        self.ui.txtRevNote.setText(self.fdata)

    def txt_to_clp(self):
        self.cursor = self.ui.txtRevNote.textCursor()
        ic("Selection start: %d end: %d" %
           (self.cursor.selectionStart(), self.cursor.selectionEnd()))
        ic(self.cursor.selectedText())
        self.clipboard.setText(self.ui.txtRevNote.toPlainText())

    def sel_txt_to_clp(self):
        self.cursor = self.ui.txtRevNote.textCursor()
        self.clipboard.setText(self.cursor.selectedText())

    def file_rename(self):
        self.highlightindex = self.treemodel.itemData(
            self.ui.treeRevNote.selectedIndexes()[0])
        ic(self.highlightindex[0])
        # self.fdir = self.dir.path() + '/'
        # self.myfname = self.fdir + self.highlightindex[0] + ".txt"
        self.text = QtWidgets.QInputDialog.getText(self,
                                                   'rename',
                                                   'rename file:',
                                                   text=self.myfname)
        if self.text[1]:
            os.rename(self.myfname, self.text[0])
            self.setuptreeview()

    def file_search(self):
        self.srch = self.ui.searchEdit.text()
        self.ui.txtRevNote.clear()
        # self.res = [i for i in self.txtbody if self.srch in i]
        self.res = [i for i in self.txtbody if self.srch in i]
        ic(self.res)
        if len(self.res):
            # self.ui.txtRevNote.setText(self.res[0])
            #self.finish_search(self.res[0])
            #if len(self.res) > 1:
            ic(len(self.res))
            # self.ui.btnNext.setEnabled(True)
            for m in self.res:
                self.finish_search(m)

        else:
            self.finish_search("not found")

    def finish_search(self, mytext):
        self.revtxt = mytext
        self.ui.txtRevNote.append(self.revtxt)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # clipboard = app.clipboard()

    main = Main()
    main.show()
    sys.exit(app.exec_())
