# Importing tkinter to make gui in python 
from tkinter import*
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf 
import PyPDF2
from gtts import gTTS
import os
  
# Initializing tk 
root = Tk() 
  
# Set the width and height of our root window. 
root.geometry("630x650+400+0") 
root.title("PDF VIEWER BY PYTHON__FEVER")
root.configure(bg="white")

def open_pdf():
   file= filedialog.askopenfilename(initialdir=os.getcwd(),title="Select a PDF", filetype=(("PDF Files","*.pdf"),("PDF Files","*.PDF"),("All Files","*.txt")))
   v1 = pdf.ShowPdf()
   v2 = v1.pdf_view(root, pdf_location = open(file,'r'), width = 77, height = 100) 
   v2.pack(pady=(0,0)) 

   

def read():
   file= filedialog.askopenfilename(initialdir=os.getcwd(),title="Select a PDF", filetype=(("PDF Files","*.pdf"),("PDF Files","*.PDF"),("All Files","*.txt")))
   pdfFileObj = open(file, "rb")
   pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
   pages = pdfReader.numPages

   for i in range(pages):
      page_text = pdfReader.getPage(i)
      mytext = page_text.extractText()
      language = 'en'
      myobj = gTTS(text=mytext, lang=language, slow=False)
      myobj.save("speech.mp3")
   
   os.system("speech.mp3")

# read()

Button(root,text="Open PDF",command=open_pdf,width=40,font='arial 20 bold',bd=4).pack()
Button(root,text="Read PDF",command=read,width=40,font='arial 20 bold',bd=4).pack()


root.mainloop()