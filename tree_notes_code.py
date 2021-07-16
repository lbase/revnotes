import sys, os
from PyQt5 import QtGui
from icecream import ic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir, QFile
# from PyQt5.QtGui import QClipboard, QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtGui import *
from tree_notes import Ui_TreeNotesWin
import tbar_rc


class Main(QtWidgets.QMainWindow, Ui_TreeNotesWin):
    """docstring for main."""
    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_TreeNotesWin()
        self.ui.setupUi(self)
        self.setuptreeview()
        self.setuptbar()

    def setuptreeview(self):
        self.dir = QDir("/home/rfile/revclips/")
        self.dir.setNameFilters(["*.txt"])
        self.lst = [os.path.splitext(x)[0] for x in self.dir.entryList()]
        self.treemodel = QStandardItemModel(0, 1)
        self.ui.treeRevNote.setModel(self.treemodel)
        for y in (self.lst):
            self.myitem = y
            self.treemodel.appendRow(QStandardItem(self.myitem))
        self.ui.treeRevNote.doubleClicked.connect(self.get_Val_edit)

    def setuptbar(self):
        self.tbarbtn01 = QtWidgets.QAction("open", self)
        self.tbarbtn01.setIcon(QIcon(":/icon/bdoccopy.png"))
        self.tbarbtn01.setStatusTip("open")
        self.tbarbtn01.triggered.connect(self.get_Val_tbar_edit)
        self.ui.toolBar.addAction(self.tbarbtn01)
        self.tbarbtn02 = QtWidgets.QAction("copy_all", self)
        self.tbarbtn02.setStatusTip("copy all")
        self.tbarbtn02.setIcon(QIcon(":/icon/cliptext.png"))
        self.tbarbtn02.triggered.connect(self.txt_to_clp)
        self.ui.toolBar.addAction(self.tbarbtn02)

        #self.ui.toolBar

    def get_Val_edit(self, val):
        self.idx = val.row()
        self.txt = self.dir.entryList()[self.idx]
        ic(val.data())
        ic(val.row())
        ic(self.txt)
        #print(val.column())
        self.fdir = self.dir.path() + '/'
        self.myfname = self.fdir + self.dir.entryList()[self.idx]
        ic(self.myfname)
        self.fod = open(self.myfname)
        self.fdata = self.fod.read()
        self.ui.txtRevNote.setText(self.fdata)

    def get_Val_tbar_edit(self):
        self.highlightindex = self.treemodel.itemData(
            self.ui.treeRevNote.selectedIndexes()[0])
        ic(self.highlightindex[0])
        self.fdir = self.dir.path() + '/'
        self.myfname = self.fdir + self.highlightindex[0] + ".txt"
        ic(self.myfname)
        self.fod = open(self.myfname)
        self.fdata = self.fod.read()
        self.ui.txtRevNote.setText(self.fdata)

    def txt_to_clp(self):

        # self.txtclp = self.ui.txtRevNote.toPlainText()
        clipboard.setText(self.ui.txtRevNote.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    clipboard = app.clipboard()

    main = Main()
    main.show()
    sys.exit(app.exec_())
