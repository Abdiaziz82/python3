class MyClass:
    # Class attribute shared by all instances
    attribute_1 = "class_attribute"  
    
     # Instance method returning a string
    def my_function(self): 
        return "am a method"
    
    #checking the value of self
    def display_self(self):  
        return self
    

object_1 = MyClass()  # Create first instance(object)
object_2 = MyClass()  # Create second instance
#object-specific attribute
object_2.attribute_2 = "i have this attribute"  
print(object_2.attribute_2) # output: i have this attribute
print(MyClass.attribute_1)  # output: class_attribute

object_1.attribute_3 = "object_attribute"  # Create instance-specific attribute_1

MyClass.attribute_1 = "hhha"  # Modify class attribute
print(MyClass.attribute_1)  # Print modified class attribute
print(object_1.my_function())  # output:am a method
#valuate the value of self and its memory address
# both will have the same memory address
print(id(object_1))  # Print object_1's memory address
print(id(object_1.display_self()))  # Print memory address of object_1 method

print(type(object_1))  # <class '__main__.MyClass'>
print(type(object_2))  # <class '__main__.MyClass'>
print(dir(object_1))  # List all attributes and methods of object_1