import os
import glob
from icecream import ic
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import sys
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
import re
from unicodedata import category
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel


class revsearch():
    def __init__(self) -> None:
        super(revsearch, self).__init__()

    def createSearchableData(self, root="/home/rfile/rev_clips"):
        self.root = root

        self.schema = Schema(title=TEXT(stored=True),path=ID(stored=True),\
                textdata=TEXT(stored=True))
        ic(self.schema)
        self.localIndexDir = os.path.join(self.root, "indexdir")
        ic(self.localIndexDir)
        if not os.path.exists(self.localIndexDir):
            os.mkdir(self.localIndexDir)
            # os.mkdir(localIndexDir + '/')

        # Creating a index writer to add document as per schema
        self.ix = create_in(self.localIndexDir, self.schema)
        self.writer = self.ix.writer()
        try:

            self.filepaths = self.TxtFileList(root)
            for path in self.filepaths:
                fp = open(path, 'r')
                text = fp.read()
                self.writer.add_document(title=(os.path.basename(path)),path=path,\
                textdata=text)

                fp.close()
            self.writer.commit()
        except:
            e = sys.exc_info()[0]
            self.writer.cancel()
            print("exception " + e)

        return self.ix.searcher()

    def TxtFileList(self, root):
        self.root = root
        self.RevTextFiles = []
        self.RevFile = []
        for file in os.listdir(self.root):
            if file.endswith(".txt"):
                self.RevTextFiles.append(os.path.join(root, file))
                # RevFile.append(file)
        return self.RevTextFiles

    def TxtFileBody(self, root):
        self.txtdir = root
        # self.txtlist2 = glob.glob(self.txtdir + "*.txt")
        #self.globtx = self.txtdir + '*.txt'
        self.txtlist2 = glob.glob(self.txtdir)
        self.bodytext = []
        for f in self.txtlist2:
            g = open(f)
            k = g.read()
            self.bodytext.append(k)
        return self.bodytext

    def TxtFiles(self, root):
        self.root = root
        self.RevFiles = []
        for file in os.listdir(self.root):
            if file.endswith(".txt"):
                self.RevFiles.append(file)
        return self.RevFiles

    def strip_nulls(self, ctrl_txt):
        ''' strip control characters
            using regex
        '''
        self.ctrl_txt = ctrl_txt
        self.t = []
        for x in self.ctrl_txt:
            self.t.append(re.sub(r"^\x00", '', x))

    def strip_cat(self, cat_txt):
        '''
        strip control characters unicodedata - category
        see http://flatboy:6969/rfile/revnotes/-/wikis/home
        '''
        self.cat_txt = cat_txt
        return "".join(ch for ch in cat_txt if category(ch)[0] != "C")


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        # self._data = data
        self.data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            # return self.data[index.row()][index.column()]
            return self.data[index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self.data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.data[0])
