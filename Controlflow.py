#Arithmetic operators
a = 6
c = 2
#Addition
print("addition :",a + c)
#subtraction
print("subtraction :",a - c)
#multiplication
print("multiplication :",a * c)
#division
print("division :",a / c)
# floor division
print(a // c)
#modulo 
print("remainder" ,a % c)
# power 
print(a ** c)

# assignment operators
a = 2
a -= 1
print(a)
#comparison operators
a = 4
b = 4
print(a == b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)

#logical operators
print(bool(True and False))
print(bool(True or False))
print(bool(-4))
x = 0
y = 5
print(x and y)
print(x or y)
print( not x)

#if else condition
status = "offline"
if status == "online":
    print("user is active")
else:
    print("user is not active")

mpesa_balance = 10
amount_to_send = 50

if mpesa_balance > amount_to_send:
    print("transaction successful")
else:
    print("you have insufficient balance")
    
marks = int(input("Enter your marks :"))

if marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

def check_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D" 
    else:
        return "F"
        
marks = 50
grade = check_grade(marks)
print(f"you have attained {marks} and your grade is {grade}")



if status == "submitted":
    message = "you have submitted your assignment"
elif status == "late":
    message = "the time for submitting has ended"
elif status == "pending":
    message = "your submsion is pending"
else :
    message = "invalid input"
    
print(message)

#dictionary mapping
status = "submited"
assignment_submissions = {
    "submitted": "you have submitted your assignment",
    "late": "the time for submitting has ended",
    "pending": "your submsion is pending",
}
print(assignment_submissions.get(status ,"invalid input"))

try:
    number1 = int(input("Enter the first number: "))
    operation = input("Enter the operation you want to perform:, +, -,  *, / ")
    number2 = int(input("Enter the second number:"))
    if operation == "+":
        print("the result is : " ,number1 + number2)
    elif operation == "-":
        print("the result is : " ,number1 - number2)
    elif operation == "*":
        print("the result is : " ,number1 * number2)
    elif operation == "/":
        try:
            print("the result is : " ,number1 / number2)
        except ZeroDivisionError:
            print("cannot divide by zero")
    else:
        print("Invalid operation")
except ValueError:
    print("please enter a valid number ")



# a = 5
# b = "5"
# try:
#     print(a + b)
# except TypeError:
#     print("invalid number")
    



    




    



