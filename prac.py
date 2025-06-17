class Person:
    def __init__(self,id,name,university):
        self.id = id
        self.name = name
        self.university = university

class Researcher:
    def __init__(self,id,name,university,department):
        self.id = id
        self.name = name
        self.university = university
        self.department = department

#multiple
class ResearchStudent(Person,Researcher):
    def __init__(self,id,name,university,department,thesis):
        Person.__init__(self,id,name,university)
        Researcher.__init__(self,id,name,university,department)
        self.thesis = thesis
    
    
class Student(Person):
    def __init__(self,id,st_name,university,course):
        Person.__init__(self,id,st_name,university)
        self.st_name = st_name
        self.course = course
        
class Adminstrator(Person):
    def __init__(self,id,ad_name,university,department):
        super().__init__(id,ad_name,university)
        self.ad_name = ad_name
        self.department = department
        
class Faculty(Student , Adminstrator):
    def __init__(self,id,st_name,ad_name ,university,course,department,school):
        Student.__init__(self,id,st_name,university,course)
        Adminstrator.__init__(self,id,ad_name,university,department)
        self.school = school
    def manage(self):
        return f"{self.ad_name} is managing {self.department} at {self.school}"
#multilevel
class SeniorStudent(Student):
    def __init__(self,id,st_name,university,course,year):
        super().__init__(id,st_name,university,course)
        self.year = year
    def get_year(self):
        return f"{self.st_name} is a {self.year} student"
        
student_1 = Student(1, "abdiaziz", "Uganda", "IT")
teacher_1 = Adminstrator(1, "abdiaziz", "Uganda", "IT")
faculty_1 = Faculty(1, "abdiaziz", "lusala", "Uganda", "IT", "IT", "Uganda")
senior = SeniorStudent(1, "abdiaziz", "Uganda", "IT", "3")
research = ResearchStudent(1, "abdiaziz", "Uganda", "IT", "IT")
print(teacher_1.department)
print(faculty_1.manage())
print(senior.get_year())
print(student_1.university)
print(research.university)































# class Person:
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name
    
# class Teacher:
#     def __init__(self,id,name,subject):
#         self.id = id
#         self.name = name
#         self.subject = subject

# class Student(Person , Teacher):
#     def __init__(self,id,name,course,subject):
#         Person.__init__(self,id,name)
#         Teacher.__init__(self,id,name,subject)
#         self.course = course

# ticha = Teacher(1, "abdiaziz", "IT")
# student_1 = Student(1, "abdiaziz", "IT" , "Mathematics")
# print(student_1.subject)


# # class Person:
# #     def __init__(self,id,name):
# #         self.id = id
# #         self.name = name
# # class Teacher:
# #     def __init__(self,id,name,subject):
# #         self.id = id
# #         self.name = name
# #         self.subject = subject
        
# # class Student(Person):
# #     def __init__(self,id,st_name,course):
# #         Person.__init__(self,id,st_name)
# #         self.st_name = st_name 
# #         self.course = course
# # class Adminstrator(Person):
# #     def __init__(self,id,ad_name,department):
# #         Person.__init__(self,id,ad_name)
# #         self.ad_name = ad_name
# #         self.department = department
# # class Faculty(Student, Adminstrator):
# #     def __init__(self, id, st_name,ad_name ,course, department, school):
# #         Student.__init__(self, id, st_name, course)
# #         Adminstrator.__init__(self, id, ad_name, department)
# #         self.school = school
        
    
# #     def manage(self):
# #         return f"{self.ad_name} is managing {self.department}"
    
# # class SeniorStudent(Student):
# #     def __init__(self, id, st_name, course, year):
# #         super().__init__(id, st_name, course)
# #         self.year = year

# # student_1 = Student(1, "abdiaziz", "IT")
# # Admin_1 = Adminstrator(1, "Lusala", "information science")
# # faculty_1 = Faculty(1, "abdiaziz", "lusala","IT", "information science" ,"SPASS")
# # print(student_1.id)
# # print(Admin_1.name)
# # print(faculty_1.manage())