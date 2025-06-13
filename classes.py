class Student:
    def __init__(self, name ,age ,grade , is_active = True):
        self.name = name
        self.age = age
        self.grade = grade
        self.is_active = is_active

    def __str__(self):
        return f"student name is {self.name} and has {self.age} years old and his grade is {self.grade}"
    def display_grade(self):
        return self.grade
    def greet_student(self):
        return f"good evenining {self.name}"
    
student_1 = Student("abdiaziz" , 20 , "A" , False)
student_2 = Student("ismail" , 22 , "B" , False)  
print(student_1)

print(student_2)
print(student_1.grade)
print(student_1.is_active)
print(student_2.name)
print(student_2.age)
print(student_2.grade)
print(student_1.display_grade())
print(student_2.greet_student())
print(dir(student_1))
print(student_1.upper())
    