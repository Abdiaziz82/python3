# super/parent/base class
class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def show_person(self):
        return f"{self.id}"
    
# child class/subclass/derived class

class Student(Person):

    def __init__(self, id, name, course):
        super().__init__(id, name)
        super().show_person()
        self.course = course
    # overiding the initial method

    def show_person(self):
        return f"{self.name}"
   
# another child class
class Teacher(Person):
    def __init__(self, id, name, subject):
        # inhering all the attributes from person
        super().__init__(id, name)
        # adding another attribute to child
        self.subject = subject


student_1 = Student(1, "abdiaziz", "IT")
teacher_1 = Teacher(1, "john", "Mathematics")
print(student_1.id)
print(teacher_1.show_person())
print(student_1.course)
print(student_1.show_person())
