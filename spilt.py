from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("origin.pdf", "rb"))

for i in range(0,inputpdf.numPages,10):
    output = PdfFileWriter()
    for j in range(10):
        output.addPage(inputpdf.getPage(i+j))
    with open("document-%s.pdf" % int(i/10), "wb") as outputStream:
        output.write(outputStream)
