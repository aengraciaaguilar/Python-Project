# Laboratory Activity # 4
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2

# utilizing the import function
import pyttsx3
import PyPDF2

# declaring variables and utilizing the open and rb function
book = open("quiz.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

# utilizing the print statements
print("number of pages in the pdf:", pages)
print("-----------------------------------"
      "\nI am now reading......Kindly listen")

# enabling the packages imported
speaker = pyttsx3.init()
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()