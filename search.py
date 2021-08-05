def createSearchableData(root):
        
        
        schema = Schema(title=TEXT(stored=True),path=ID(stored=True),\
                content=TEXT,textdata=TEXT(stored=True))
        ic(schema)        
        if not os.path.exists("indexdir"):
            os.mkdir("indexdir")

        # Creating a index writer to add document as per schema
        ix = create_in("indexdir",schema)
        writer = ix.writer()

        filepaths = [os.path.join(root,i) for i in os.listdir(root)]
        for path in filepaths:
            fp = open(path,'r')
           # ic(path)
            text = fp.read()
            # ic(text)
            writer.add_document(title=path.split("/")[4], path=path,\
            content=text,textdata=text)
            fp.close()
        writer.commit()
        return ix.searcher()
        