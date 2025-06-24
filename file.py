#create a file
file = open("first_file.txt" , mode="w")
file.write("my file")

#read file
my_file = open("first_file.txt")
print(my_file.read())
my_file.close()
#append content into a file
with open("python.txt" , "a" )as python_file:
    for txt in range(7):
        python_file.write("python is  \n")
        
#read docx file in binary       
with open("/mnt/c/Users/Abdiaziz/Downloads/MANAGEMENT OF INFORMATION SYSTEMS CAT.docx" , "rb") as python_file:
    print(python_file.read())

#open and read docx file using docx library 
from docx import Document
doc = Document("/mnt/c/Users/Abdiaziz/Downloads/MANAGEMENT OF INFORMATION SYSTEMS CAT.docx" )
for paragraph in doc.paragraphs: 
    print(paragraph.text)
