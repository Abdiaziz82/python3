class Student:
    #class attribute
    university_name = "Garissa university"
    #track the total number of students
    all_students = []
    total_students = 0 
    
    def __init__(self,name,age,email,grade,is_present):
        self.name = name
        self.age = age
        self.email = email
        self.grade = grade
        self.is_present = is_present
        #add each object automatically to the list
        Student.add_student(self)
        
    #class method
    @classmethod
    def add_student(cls ,student):
        cls.all_students.append(student)
        cls.total_students += 1
    @classmethod
    def get_student(cls):
        return cls.total_students

    @classmethod
    #print all the object names
    def show_all_students(cls):
        for student in cls.all_students:
            print(f"{student.name}")
    
    #class method to change class attribute
    @classmethod
    def change_university(cls,univ_name):
        cls.university_name = univ_name
        print(f"i am : {cls}")
        return f"university name updated to {univ_name}"
    
    def disp_student_name(self):
        return f"{self.name}"
   
if __name__ == "__main__": 
    print(f"the classmethods.py module name {__name__}") 
    
    s1 = Student("abdiaziz" , 20 ,"abdiazizgmail.com" , "A" , True)
    s2 = Student("Hima" , 20 ,"halima@gmail.com" , "B" , True)
    s3 = Student("lima" , 20 ,"halima@gmail.com" , "B" , True)
    s4 = Student("Haa" , 20 ,"halima@gmail.com" , "B" , True)
    s5 = Student("ma" , 20 ,"halima@gmail.com" , "B" , True)
    
    print(Student.university_name)
    s1.university_name = "University of Nairobi"
    
    print(s1.university_name)
    print(Student.change_university("MKU"))
    print(Student.university_name)
    print(s1.change_university("GAU"))
    print(Student.get_student())
    print(Student.show_all_students())    