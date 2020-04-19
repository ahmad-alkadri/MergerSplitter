from PyPDF2 import PdfFileMerger
from tkinter import filedialog as fd
from tkinter import Tk

root = Tk()
root.withdraw()

pdfs = fd.askopenfilenames(title = "Select the PDF files")

outnamepath = fd.asksaveasfilename(title = "Name output file",
    filetypes = (("PDF files","*.pdf"),("all files","*.*")))
    
root.update()

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(outnamepath)
merger.close()