#while loops
i = 1
while i <= 10:
    print(i)
    i= i+1
     #increment
    
j = 10
while j >= 1:
    print(j)
    j-=1
    
#multiplication table
number = int(input("Enter a number: "))

multiply_by = 1
while multiply_by <= 10:
    product = number * multiply_by
    print(f"{number} * {multiply_by} = {product}")
    multiply_by += 1 # Increase multiply_by by 1 1 for the next iteration

#for loop

name = "abdullahi"
for letter in name: # Loop through each letter in the name
    print(letter)

student_names = ["abdi" ,"abdullahi", "yussuf"]
for name in student_names:
    print(name)

for num in range(1,6):
    print(num)
    
#break in loops
word = ""
while word != "exit":
    word = input("Enter something:  ")
    if word == "exit":
        break
    else:
        print(f"you typed : {word}")
        
#continue
for num in range(1,11):
    if num % 2 == 0:
        continue
    print(num)

total = 0
for i in range(1,101):
    total+=i  
print(total)

student_scores = [70,30,50,60,30]
highest_score = 0
runner_up = 0
for score in student_scores:
    if score > highest_score:
        runner_up = highest_score
        highest_score = score
    elif score > runner_up:
        runner_up = score
print(f"the highest score is ,{highest_score}")
print(f"the second person is {runner_up}")

#nested_loop

#outerloop
outer_loop = 1
while outer_loop <= 3:
    print(f"this is the {outer_loop} iteration of the outer loop")
    inner_loop = 1
    while inner_loop <= 4:
        product = outer_loop * inner_loop
        print(f"{outer_loop} * {inner_loop} = {product}")
        inner_loop +=1
    outer_loop +=1
    print("---------------")
    


numbers = [1,2,3,4,5]
modified_numbers = []
filtered_numbers = []
for num in numbers:
    if num % 2 == 0:
        result = num ** 2
        modified_numbers.append(result)
print(modified_numbers) 
    
#list_comprehension
squared_numbers =[num ** 2 for num in numbers if num % 2 == 0]
print(squared_numbers)

students = ["ahmed" ,"ridwan" ,"abdullahi" ,"abdiaziz"]
email_address = []
for student in students:
    web_mail = student + "@oasis.ac.ke"
    email_address.append(web_mail)
print(email_address)

email_address = [student + "@oasis.gau.ac.ke" for student in students]
print(email_address)










    

    
    
