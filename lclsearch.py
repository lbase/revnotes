import os
import glob
from icecream import ic
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import sys
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
# test note from bubba


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

            self.filepaths = self.txtfilelist(root)
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