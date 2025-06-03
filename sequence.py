# LISTS
# Lists store ordered, indexed, mutable group of values
# Lists allow duplicates

# Create a list of numbers with duplicates
my_list = [1,2,3,4,5,5,5]
# Print the list: [1, 2, 3, 4, 5, 5, 5]
print(my_list)
# Print the type: <class 'list'>
print(type(my_list))
# Print the second item (index 1): 2
print(my_list[1])
# Change the second item to 8
my_list[1] = 8
# Slice the list (index 0 to 2); this doesn't modify the list or print anything
my_list[0:3]
# Print the list after modification: [1, 8, 3, 4, 5, 5, 5]
print(my_list)
# Remove and return the last item (5)
my_list.pop()
# Reverse the list order
my_list.reverse()
# Print the reversed list: [5, 5, 4, 3, 8, 1]
print(my_list)

# Create a list of student names
students = ["abdullahi", "halima", "ahmed", "faiza", "abdiaziz"]
# Print every second item from index 0 to 3: ['abdullahi', 'ahmed']
print(students[0:4:2])
# **ERROR**: Index out of range
# The list has 5 items (indices 0 to 4), but index 5 is accessed, causing an IndexError
print(students[5])

# TUPLES
# Tuples store ordered, indexed, immutable group of values
# Tuples allow duplicates

# Create a tuple of numbers
numbers = (1,2,3,5,6)
# Print the tuple: (1, 2, 3, 5, 6)
print(numbers)
# Print the type: <class 'tuple'>
print(type(numbers))
# Print the first item: 1
print(numbers[0])
# **ERROR**: TypeError: 'tuple' object does not support item assignment
# Tuples are immutable, so you can't change their values
numbers[1] = 9 
# **ERROR**: AttributeError: 'tuple' object has no attribute 'pop'
# Tuples don't have a pop() method because they can't be modified
numbers.pop()
# This line won't run due to the errors above
print(numbers)

# SETS
# Sets store unordered, immutable group of values (not indexed)
# Sets don't allow duplicates
# Note: The comment saying sets are "indexed" is incorrect; sets are unordered and not indexed

# Create a set of colors (duplicates are removed)
colors = {"blue", "green", "purple", "blue"}
# Print the type: <class 'set'>
print(type(colors))
# Print the set: {'blue', 'green', 'purple'} (only unique values)
print(colors)

# Create a list with duplicates
my_numbers = [1,2,3,4,4,4,3]
# Convert list to set to remove duplicates: {1, 2, 3, 4}
print(set(my_numbers))
# Print the first item of the list: 1
print(my_numbers[0])

# DICTIONARIES
# Dictionaries store key-value pairs, mutable, and keys are unique

# Create a dictionary
student = {
    "name": "halima",
    "age": 23,
    "gender": "female",
    "is_online": True,
     6: "ahhh"
}
# Print the dictionary
print(student)
# Print the type: <class 'dict'>
print(type(student))
# Print the value for key 'name': halima
print(student['name'])

# Safely get value for 'number'; returns "key is not found" since 'number' doesn't exist
print(student.get('number', "key is not found"))

# Delete the key-value pair with key 6
del student[6]
# Print the dictionary after deletion
print(student)

# Update the 'name' value to "abdullahi"
student['name'] = "abdullahi"
# Print the updated dictionary
print(student)

# IMPLICIT CONVERSION
# Python automatically converts types in some operations

# Integer + float results in a float: 5.5
a = 3
b = 2.5
print(a + b)

# EXPLICIT CONVERSION
# Manually convert types

# Convert string "2" to integer and add to 12: 14
x = "2"
y = 12
print(int(x) + y)

# Get user input (string)
name = input("enter your name: ")
# Get user input, convert to integer
age = int(input("enter your age: "))
# **POTENTIAL ERROR**: ValueError
# If the user enters a non-integer (e.g., "abc") for age, int() will fail
print(f"your name is {name} and your age is {age}")

# Convert binary string "1110" to decimal: 14
print(int("1110", 2))

# ASSERTION
# Check if a condition is true; raises an error if false

# Define a variable
a = 5
# **ERROR**: AssertionError
# The condition a == 7 is false (5 != 7), so this raises an AssertionError
assert a == 7