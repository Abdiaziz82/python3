# Define a function called my_function that does nothing (placeholder)
def my_function():
    # 'pass' is used when you want to create a function but leave its implementation empty for now
    pass

# Variables store data (like names) that can be reused or changed
user_name = "halima"
welcome_message = f"hello {user_name} welcome to our app"
print(welcome_message)

user_name = "Ahmed"
welcome_message = f"hello {user_name} welcome to our app"
print(welcome_message)

user_name = "Amina"
welcome_message = f"hello {user_name} welcome to our app"
print(welcome_message)

# Functions let you reuse code efficiently, avoiding repetition for tasks like printing welcome messages
def welcome_user(user_name):
    welcome_message = f"hellooooo {user_name} welcome to our app"
    return welcome_message

print(welcome_user("halima"))
print(welcome_user("ahmed"))
print(welcome_user("Amina"))

# --- Function with default parameters ---
# Define a function called add_numbers that takes three parameters: a, b, and c
# 'c' has a default value of 5, meaning if no value is provided, 5 is used
def add_numbers(a, b, c=5):
    # Add the three parameters and store the result
    result = a + b + c
    # Print the result
    print(result)

# Call the function with only two arguments; c will use its default value (5)
add_numbers(2, 3)

# --- Function with keyword arguments ---
# Define a function called keyword that takes three parameters: name, age, and gender
# 'gender' has a default value of "female"
def keyword(name, age, gender="female"):
    # Print the name
    print(name)
    # Print the age
    print(age)
    # Print the gender
    print(gender)

# Call the function using keyword arguments (specifying parameter names)
keyword(name="halima", age=20)


# --- Function with variable arguments (*args and **kwargs) ---
# Define a function called students that accepts:
# *args: a variable number of non-keyword arguments (stored as a tuple)
# **kwargs: a variable number of keyword arguments (stored as a dictionary)
def students(*args, **kwargs):
    # Print the second argument from args (index 1, since indexing starts at 0)
    print("student at second position is ", args[1])
    # Print all keyword arguments as a dictionary
    print(kwargs)
    # Print the value of the 'age' key from kwargs
    print("student has age of", kwargs["age"])

# Call the function with multiple non-keyword arguments and keyword arguments
students("halima", "ahmed", "faiza", "abdiaziz", "ali", age=20, course="IT")

product = "laptop"

def function():
    name = "halima"
    print(name)
    
function()
# print(name)

    
product = "laptop"

def my_product():
    global product
    product = "phone"
    print(product)
my_product()
print(product)








    
