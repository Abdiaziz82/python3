# # from os import *
# # print(name)

# # import platform
# # print(platform.system())

# # import sys
# # print(sys.version)
# # # print(dir(os))
# import csv

# # Sample data (list of rows)
# import csv

# data = [
#     {"name": "Abdiaziz", "age": 22, "email": "abdiaziz@example.com"},
#     {"name": "Asha", "age": 24, "email": "asha@example.com"},
# ]

# # Write to CSV using DictWriter
# with open("students.csv", "w", newline="") as file:
#     fieldnames = ["name", "age", "email"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerows(data)
# from docx import Document
# doc = Document("/mnt/c/Users/Abdiaziz/Downloads/MANAGEMENT OF INFORMATION SYSTEMS CAT.docx")
# for paragraph in doc.paragraphs:
#     print(paragraph.text)
    
# file = open("file.txt" , "r" )
# print(file.read())
# file.close()

# with open("abdi.txt" , mode="w") as file:
#     file.write("hhdeei")

# import functions
# from classmethods import Student
# student_3 = Student("abdi" , 60 ,"A" , 50 , False) 
# print(student_3.name)
# # print(functions.welcome_user("abdiaziz")) 

# import csv

# import csv
# with open('protagonist.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
    
#     writer.writerow(["SN", "Movie", "Protagonist"])
#     writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
#     writer.writerow([2, "Harry Potter", "Harry Potter"])
    
# print(writer)

# open file

file = open("abdi.txt" , "r" )
print(file.read())
file.close()
with open("fil.txt" , mode="w") as file:
    for i in range(4):
        file.write("hhdeei \n")