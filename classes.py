class Student:
    #init constructor
    def __init__(self, name , age , grade, marks , is_active = True,):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks
        self.is_active = is_active
        
    # string representation of student object
    def __str__(self):
        return f"student name is {self.name} and has {self.age} years old and his grade is {self.grade}"
    def display_grade(self):
        return self.grade
    def greet_student(self): # method to greet student
        return f"good evenining {self.name}"


    def get_marks(self):
        print("getting marks")
        return self._marks
    def set_marks(self , marks):
        print("setting marks")
        if marks > 100: 
            print("invalid marks")
            self._marks = None
        else:
            self._marks = marks
    
    def del_marks(self):
        print("deleting marks")
        del self._marks

    marks = property(get_marks , set_marks ,del_marks , "this is a protected marks ")

student_1 = Student("abdiaziz" , 20 ,"A" , 50 , False) # create first student object
student_2 = Student("ismail" , 21 ,"B" , 60, False) # create second student object
print(student_1.marks)
print(student_1.marks)
student_1.marks = 70
print(student_1.marks)
del student_1.marks
help(Student.marks)
print(Student.marks.__doc__)


# print(student_1)
# print(student_2)
# print(student_1.grade)
# print(student_1.is_active)
# print(student_2.name)
# print(student_2.grade)
# print(student_1.display_grade())
# print(student_2.greet_student())
print(getattr(student_1 ,"nam" , "attribute doesnt exist" ))
setattr(student_1 ,"grade" , "D")
print(hasattr(student_1 ,"grad"))
print(student_1.grade)
del student_1.grade
delattr(student_1 , "grade")
print(student_1.grade)
# print(dir(student_1))
# print(student_1.upper())
    