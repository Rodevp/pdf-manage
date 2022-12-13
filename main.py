import PyPDF2 as pdf
import os

merger = pdf.PdfFileMerger()

for file in os.listdir(os.curdir) :

    if file.endswith(".pdf") :
        print(f"file -> {file}")
        merger.append(file)

    merger.write("unique.pdf")

    
