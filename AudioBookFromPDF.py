import pyttsx3
from PyPDF2 import PdfReader

book = open('sample.pdf','rb')

reader=PdfReader(book)
num_pages=len(reader.pages)

play = pyttsx3.init()
print("Playing Audio Book")

for num in range(0,num_pages):
    page=reader.pages[num]
    data=page.extract_text()
    play.say(data)
    play.runAndWait()
