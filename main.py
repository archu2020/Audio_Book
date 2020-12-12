import pyttsx3
import PyPDF2
book=open("Statistic.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
# print(pages)
for i in range (4,pages):
    page=pdfReader.getPage(4)
    text=page.extractText()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
