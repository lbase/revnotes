import sys, os
from PyQt5 import QtGui
from icecream import ic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir, QFile
# from PyQt5.QtGui import QClipboard, QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtGui import *
from tree_notes import Ui_TreeNotesWin
import tbar_rc
from lclsearch import revsearch

# ic.disable()


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
        self.dir = revsearch.TxtFileList(self, "/home/rfile/rev_clips/")
        ic(self.dir)
        self.lst = revsearch.TxtFiles(self, "/home/rfile/rev_clips")
        ic(self.lst)
        self.txtbody = revsearch.TxtFileBody(self,
                                             "/home/rfile/rev_clips/*.txt")
        ic(self.txtbody)
        self.treemodel = QStandardItemModel(0, 1)
        self.ui.treeRevNote.setModel(self.treemodel)
        for y in (self.lst):
            self.myitem = y
            self.treemodel.appendRow(QStandardItem(self.myitem))
        self.ui.treeRevNote.clicked.connect(self.get_Val_edit)

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
        self.tbarbtn03 = QtWidgets.QAction("rename", self)
        self.tbarbtn03.setStatusTip("rename file")
        self.tbarbtn03.setIcon(QIcon(":icon/docrename.png"))
        self.tbarbtn03.triggered.connect(self.file_rename)
        self.ui.toolBar.addAction(self.tbarbtn03)
        #menu file rename
        self.ui.actionReName.triggered.connect(self.file_rename)
        #self.ui.toolBar

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

    def file_rename(self):
        self.highlightindex = self.treemodel.itemData(
            self.ui.treeRevNote.selectedIndexes()[0])
        ic(self.highlightindex[0])
        self.fdir = self.dir.path() + '/'
        self.myfname = self.fdir + self.highlightindex[0] + ".txt"
        self.text = QtWidgets.QInputDialog.getText(self,
                                                   'rename',
                                                   'rename file:',
                                                   text=self.myfname)
        if self.text[1]:
            os.rename(self.myfname, self.text[0])
            self.setuptreeview()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # clipboard = app.clipboard()

    main = Main()
    main.show()
    sys.exit(app.exec_())
