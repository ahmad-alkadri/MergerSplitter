from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog as fd
from tkinter import Tk

root = Tk()
root.withdraw()

pdfname = fd.askopenfilename(title = "Select the PDF file")

inputpdf = PdfFileReader(open(pdfname, 
    "rb"))

outfilenamepattern = pdfname + '-page%s.pdf'

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(outfilenamepattern % i, "wb") as outputStream:
        output.write(outputStream)