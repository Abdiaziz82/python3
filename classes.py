class Student:
    def __init__(self, name ,age ,grade , is_active = True):
        self.name = name
        self.age = age
        self.grade = grade
        self.is_active = is_active
    
    @property 
    def grade(self):
        print("getting grade")
        return self._grade
    @grade.setter
    def grade(self,grade):
        print("setting grade")
        
        if grade == "A" :
            print(f"setting grade to {grade}")
            self._grade = grade
        else :
            print(f"grade must be between 0 and 100")
    @grade.deleter
    def grade(self):
        print("deleting grade")
        del self._grade
        

    def get_age(self):
        print("getting grade")
        return self._age
    
    def set_age(self,age):
        print("setting age")
        
        if age >= 40 :
            print(f"setting grade to {age}")
            self._age = age
        else :
            print(f"age must be greater than 40")

    def del_age(self):
        print("deleting age")
        del self._age
        
    def __str__(self):
        return f"student name is {self.name} and has {self.age} years old and his grade is {self.grade}"
    def display_grade(self):
        return self.grade
    def greet_student(self):
        return f"good evenining {self.name}"
    
    age = property(get_age, set_age , del_age, "thiss sishdue")
    
student_1 = Student("abdiaziz" , 20 , "A" , False)
# student_2 = Student("ismail" , 22 , "B" , False)  
    
print(student_1.grade)

print(student_1.grade)

# student_1.grade = 100
# print(student_1.grade)
# student_1.age = 85
# print(student_1.age)
# del student_1.age
# print(Student.age.__doc__)

# print(student_2)
# print(student_1.grade)
# print(student_1.is_active)
# print(student_2.name)
# print(student_2.age)
# print(student_2.grade)
# print(student_1.display_grade())
# print(student_2.greet_student())
# print(dir(student_1))
# print(student_1.upper())
    