import PyPDF2 
import textract

file = open("test.pdf",'rb')
pdf_reader = PyPDF2.PdfFileReader(file)

num_pages = pdf_reader.numPages
count = 0
text = "" #read each page.
while count < num_pages:
    pageObj = pdf_reader.getPage(count)
    count +=1
    text += pageObj.extractText()

# text = textract.process("test.pdf", extension="pdf")
# text = textract.process("test.pdf", method='tesseract', language='eng')

print(text)

write_file = open("test.txt","w", encoding="utf-8")
write_file.write(text)

file.close()
write_file.close()