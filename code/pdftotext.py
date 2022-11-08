import PyPDF2 
import textract

def convert_pdf_to_txt(path):
    file = open(path,'rb')
    pdf_reader = PyPDF2.PdfFileReader(file)

    num_pages = pdf_reader.numPages
    count = 0
    text = "" 
    while count < num_pages:
        pageObj = pdf_reader.getPage(count)
        count +=1
        text += pageObj.extractText()

    # text = textract.process("test.pdf", extension="pdf")
    # text = textract.process("test.pdf", method='tesseract', language='eng')

    txt_filename = path[0:-4] + ".txt"
    write_file = open(txt_filename,"w", encoding="utf-8")
    write_file.write(text)
    file.close()
    write_file.close()

convert_pdf_to_txt("./../pdf/10.1257_aer.112.1.i.pdf")