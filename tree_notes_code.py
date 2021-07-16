import sys, os
from icecream import ic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir, QFile
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
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
        self.ui.treeRevNote.doubleClicked.connect(self.getValue)

    def setuptbar(self):
        self.tbarbtn01 = QtWidgets.QAction("open", self)
        self.tbarbtn01.setIcon(QIcon(":/icon/bdoccopy.png"))
        self.tbarbtn01.setStatusTip("open")
        self.ui.toolBar.addAction(self.tbarbtn01)

        #self.ui.toolBar

    def getValue(self, val):
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
