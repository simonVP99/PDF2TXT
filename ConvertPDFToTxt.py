import PyPDF2
 
#create file object variable
#opening method will be rb
pdffileobj=open('file.pdf','rb')
 
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
 
#This will store the number of pages of this pdf file
x=pdfreader.numPages
 
#create a variable that will select the selected number of pages
for page in range(x):
	pageobj=pdfreader.getPage(page)
 
#create text variable which will store all text datafrom pdf file
	text=pageobj.extractText()
	file1=open(r"YOURPATH/file.txt","a")
	file1.writelines(text)