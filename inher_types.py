

class Person:
    def __init__(self,id,name,uni_name):
        self.id = id 
        self.name = name
        self.uni_name = uni_name
# single inheritance   
class Student(Person):
    def __init__(self,id,st_name, uni_name, course):
        Person.__init__(self ,id, st_name ,uni_name)
        self.st_name = st_name
        self.course = course
        
class Researcher:    
    def __init__(self,id,name,uni_name,age):
        self.id = id 
        self.name = name
        self.uni_name = uni_name
        self.age = age
class Adminstrator(Person):
    def __init__(self,id, ad_name, uni_name,department):
        Person.__init__(self,id,ad_name,uni_name)
        self.ad_name = ad_name
        self.department = department
        
#hybrid inheritance      
class Faculty(Student, Adminstrator):
    def __init__(self, id,st_name, ad_name ,uni_name, course,department,school):
        Student.__init__(self,id,st_name,uni_name,course)
        Adminstrator.__init__(self,id,ad_name,uni_name,department)
        self.school = school
    
    def manage(self):
        return f"{self.ad_name} manages {self.department} in {self.school}"
    def show_reg_student(self):
        return f"{self.st_name} is a student in {self.school}"
# multiple inheritance
class ResearchStudent(Person,Researcher):
    def __init__(self,id,name,uni_name, project,age):
        Person.__init__(self,id,name,uni_name)
        Researcher.__init__(self,id,name,uni_name,age)
        self.project = project
    def show_researcher(self):
        return f"{self.name} is current doing {self.project} and is {self.age} years old"
        
#multilevel inheritance
class SeniorStudent(Student):
    def __init__(self,id,name, uni_name, course,role):
        super().__init__(id,name,uni_name,course)
        self.role = role

f_student = Student(1, "abdiaziz", "gau" ,"IT")
researcher_1 = ResearchStudent(2,"ismail","MKU" , "web app", 20)
senior_stud = SeniorStudent(3,"halima" ,"GAU" , "Nursing","secretarygeneral")
f_faculty = Faculty(4 ,"abdullahi", "Lusala" ,"Garissauniversity" ,"IT","information & CS", "SPASS")
print(f_faculty.school)
print(senior_stud.name ,senior_stud.role)
print(researcher_1.show_researcher())
print(f_student.id)
print(f_faculty.manage())
print(f_faculty.show_reg_student())
        
    
    