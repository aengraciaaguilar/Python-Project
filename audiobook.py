# Laboratory Activity # 4
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2

# utilizing the import function
import pyttsx3
import PyPDF2

# declaring variables
book = open("quiz.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages


