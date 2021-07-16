import sys, os
from icecream import ic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir, QFile
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from tree_notes import Ui_TreeNotesWin


class Main(QtWidgets.QMainWindow, Ui_TreeNotesWin):
    """docstring for main."""
    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_TreeNotesWin()
        self.ui.setupUi(self)
        self.setuptreeview()

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

    def getValue(self, val):
        #print(val.data())
        #print(val.row())
        #print(val.column())
        self.fdir = self.dir.path() + '/'
        self.myfname = self.fdir + (val.data() + ".txt")
        ic(self.myfname)
        self.fod = open(self.myfname)
        self.fdata = self.fod.read()
        self.ui.txtRevNote.setText(self.fdata)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
