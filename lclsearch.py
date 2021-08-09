import os
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

        def createSearchableData(root):
            self.root = root
            # don't store index in same dir as text files ...
            self.indexdir = "home/rfile/index/revnotes"

            self.schema = Schema(title=TEXT(stored=True),path=ID(stored=True),\
                    content=TEXT,textdata=TEXT(stored=True))

            if not os.path.exists(self.indexdir):
                os.mkdir(self.indexdir)

            # Creating a index writer to add document as per schema
            self.ix = create_in(self.indexdir, self.schema)
            self.writer = self.ix.writer()

            self.filepaths = [
                os.path.join(self.root, i) for i in os.listdir(self.root)
            ]
            for path in self.filepaths:
                fp = open(path, 'r')
                # ic(path)
                text = fp.read()
                # ic(text)
                self.writer.add_document(title=path.split("/")[4], path=path,\
                content=text,textdata=text)
                fp.close()
            self.writer.commit()
            return self.ix.searcher()
