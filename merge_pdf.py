from PyPDF2 import PdfMerger

pdfs = ['mybook_01.pdf', 'mybook_02.pdf', 'mybook_03.pdf', 'mybook_04.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("mybook.pdf")
merger.close()