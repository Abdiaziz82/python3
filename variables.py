# coment
# print("hello world")

# Assigning a string value to a variable and printing it
variable = "i love python"
print(variable)

# Variable reassignment: the value of 'name' changes to "halima"
name = "abdi"
name = "halima"  # this overwrites the previous value
print(name)  # Output: halima

# Multiple  assignment and swapping of variables
a, b, c = 1, 2, 3  # a=1, b=2, c=3
a, b, c = c, b, a  # swapping: a=3, b=2, c=1
print(a, b, c)  # Output: 3 2 1

# Assigning multiple values and printing them with newline separator
name, age = "abdi", 20
print(name, age, sep="\n")  # 'sep="\n"' prints each value on a new line

# Print with custom ending (stays on the same line)
print("hello", end=" ")  # stays on the same line
print("world")  # Output: hello world

# Writing text to a file
file = open("hello.txt", "w")  # opens a file in write mode
print("hello world", file=file)  # writes to hello.txt instead of the screen

# -----------------------------
# Rules for naming variables:
# -----------------------------
# 1. Do NOT start with numbers or special characters
person = "gggy"

# 2. Do NOT use spaces, use snake_case instead
student_name = "ahmed"
print(student_name)

# 3. You can add numbers after the name
person_1 = "ahmedd"
print(person_1)

# 4. Stick to descriptive variable names
user_name = "ali"
print(user_name)

# 5. You can store and print numbers too
number = 4
print(number)

# 6. Do NOT use Python reserved keywords like 'class', 'if', 'def', etc.
# class = "python"  # ❌ invalid
# print(class)

#  with Strings

employee_name = '    Abdiali    '  # string with extra spaces
print(employee_name[-1])  # prints the last character (space)
print(type(employee_name))  # <class 'str'>
print(employee_name.upper())  # converts to uppercase
print(employee_name.lower())  # converts to lowercase
print(employee_name.split())  # splits into a list of words
print(employee_name.lstrip())  # removes leading spaces

name = "hello"
print(name.startswith("i"))  # checks if the string starts with 'i' (False)

# -----------------------------
# Working with Numbers
# -----------------------------
number = 10
print(type(number))  # <class 'int'>

a = 1.5
print(type(a))  # <class 'float'>

complex_number = 2j
print(type(complex_number))  # <class 'complex'>

# -----------------------------
# Boolean Values (True / False)
# -----------------------------
is_logged_in = True
print(type(is_logged_in))  # <class 'bool'>

is_admin = False
print(is_admin)  # Output: False

# -----------------------------
# Using f-strings for formatting output
# -----------------------------
person_name = "john kamau"
person_age = 50
print(f"my name is {person_name} and i am {person_age} years old")

user_name = "abdi"
print(f"hello {user_name} , please click this link to reactivate your ")
