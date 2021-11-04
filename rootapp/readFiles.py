class ReadFiles:
    def __init__(self):
        pass

    def readDoc(self, fpath):
        import docx
        doc = docx.Document(fpath)
        filecontent = []
        for para in doc.paragraphs:
            filecontent.append(para.text)
        
        return "".join(filecontent)
    
    def readText(self, fpath):
        f = open(fpath)
        filecontent = "".join(f.readlines())
        return filecontent

    def readPdf(self, fpath):
        from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
        from pdfminer.layout import LAParams
        from pdfminer.converter import TextConverter
        from io import StringIO
        from pdfminer.pdfpage import PDFPage


        resource_manager = PDFResourceManager(caching=True)

        out_text = StringIO()

        codec = 'utf-8'

        laParams = LAParams()

        text_converter = TextConverter(resource_manager, out_text, laparams=laParams)

        fp = open(fpath, 'rb')#my read binary mode

        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
            interpreter.process_page(page)

        text = out_text.getvalue()
        
        fp.close()
        text_converter.close()
        out_text.close()

        return text