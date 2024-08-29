#英文表达真他娘的费劲
#English is easy to use。
from PyPDF2 import PdfFileWriter, PdfFileReader
#打开pdf文件
#Open pdf file
inputpdf = PdfFileReader(open("origin.pdf", "rb"))
#从第0页开始，到最后一页，每10页取一页作为首页
#Set the first page as the new file's first page, and obtain after 9 pages. 
for i in range(0,inputpdf.numPages,10):
    #将原pdf文件写入
    #Write the original pdf file into the new one.
    output = PdfFileWriter()
    #写入10页
    #Save 10 pages.
    for j in range(10):
        output.addPage(inputpdf.getPage(i+j))
    #保存,名称是第i/10个。
    #Save file number is i/10.
    with open("document-%s.pdf" % int(i/10), "wb") as outputStream:
        output.write(outputStream)
