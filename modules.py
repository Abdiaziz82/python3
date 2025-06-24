# import os
# from platform import system
# from decorators import add_num ,require_login
from classmethods import Student

# print(os.listdir())
student_6 = Student("mohamed" , 30 ,"halima@gmail.com" , "C" , False)
print(student_6.name)

print(f"the modules.py name is {__name__}")
# print(add_num(6,8))

# @require_login
# def access_admin_dash():
#     print("accessing dashboard")
    
# access_admin_dash()
    
# print(system())
# print(os.name)

# print(__name__)
# print(__package__)
