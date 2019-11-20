import os
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
NOTEPATH = "/home/mtizim/Notatki"
assert os.getcwd()==NOTEPATH, "Wykonaj z dobrego folderu a nie"

folders = ["Algebra","Analiza","Elitm"]

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def is_numbered_pdf(name):
    if name[-4:]!= ".pdf": return False
    s = name.split(".")[0]
    try:
        int(s)
    except:
        return False
    return True

def merge_pdfs_from_path(path):
    pdfs = [name for name in os.listdir(path[:-1]) if is_numbered_pdf(name)]
    pdfs = sorted(pdfs,key=lambda s: int(s.split(".")[0]))
    pdfs = [path + name for name in pdfs]
    merge_pdfs(pdfs,path+"merged")

for folder in folders:
    merge_pdfs_from_path(NOTEPATH +"/"+ folder + "/")


