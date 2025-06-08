# # # # user_input = int(input("Enter the number you want to multiply with:"))
# # # # i = 10
# # # # while i > 0:
# # # #     result = user_input * i
# # # #     print(f"{user_input} * {i} = {result}")
# # # #     i -= 1

# # # # j = 0
# # # # while j <= 5:
# # # #     print("hello")
# # # #     if j == 3:
# # # #         break
# # # #     j += 1
    
# # # # i = 0
# # # # while i <= 10:
# # # #     if i % 2 == 0:
# # # #         i+=1
# # # #         continue
# # # #     print(i)
# # # #     i += 1
    
    
# # # j = 5 
# # # while j >= 0:
# # #     if j == 3:
# # #         j -=1
# # #         continue
# # #     else :
# # #         print(j)
# # #         j -= 1

# # # i = 0
# # # while i <= 5:
# # #     if i % 2 != 0:
# # #         i+=1
# # #         continue
# # #     print(i)
# # #     i+=1
    
# # # word = ""

# # # while word != "quit":
# # #     word = input("Enter a word: ")
# # #     if word != "quit":
# # #         print(f"You typed {word}")
# # #     else:
# # #         print("Goodbye")

# i = 1
# while i <= 3:
#     print("table of", i)
#     j = 1
#     while j <= 3:
#         total = i * j
#         print(f"{i} * {j} = {total}") 
#         j += 1
#     print("---")
#     i += 1
     
     
    
# # students = ["abdullahi", "halima", "ahmed", "faiza", "abdiaziz"]
# # for student in students:
# #     print(student)


# # highest_score = 0
# # student_scores = [12,45,59,80,90] 
# # for score in student_scores:
# #     if score > highest_score:
# #         highest_score = score
# # print(f"The highest score is {highest_score}")  


# # total = 0 
# # for number in range(1,101):
# #     total += number
# # print(f"The total is {total}"  )

# # scores = [20,30,50]
# # #Print highest score using max
# # print(max(scores))

# # for i in range(7):
# #     print(i , end=" ")
 
# # name = "abdi"
# # for letter in name:
# #     if letter == "b":
# #         continue
# #     else:
# #         print(letter)

# # numbers = [1,2,3,4]
# # for num in numbers:
# #     if num == 3:
# #         break
# #     print(num)

# total = 0
# for n in range(1,101):
#     total += n
# print(f"The total is {total}")

# highest_score = 0
# runner_up = 0
# scores =[97,12,34,54,90]
# for score in scores:
#     if score > highest_score: 
#         runner_up = highest_score
#         highest_score = score
#     elif score > runner_up :
#         runner_up = score
# print(f"The highest score is {highest_score}")
# print(f"the runner up is {runner_up}")


# for row in range(1,5):
#     for col in range(6):
#         print("*" ,end=" ")
#     print()

# students = ["abdi", "ali" , "abdullahi" ,"aisha"]
# for classes in range(4):
#     print(f"------class------------ {classes}")
#     for student in students:
#         print(student ,end=" " )
#     print()
    
    

# for num in range(1,6):
#     print(f"table of {num}")
#     for i in range(1,5):
#         total = num * i
#         print(f"{num} * {i} = {total}")
#     print("-------------------------")
    
# for j in range(1,3):
    
#     for n in range(1,3):
#         print("i'm the inner")
#     print()


# numbers = [1,2,3,4 , 6, 8]
# new_numbers = []
# filtered_numbers =[]

# for num in numbers:
#     # new_numbers.append(num **2)
#     if num % 2 == 0:
#         filtered_numbers.append(num **2)
# # print(new_numbers)
# print(filtered_numbers)

# my_numbers = [20,35,40]
# filtered = [num **2 for num in my_numbers if num % 2 == 0]
# print(my_numbers)

# names = ["abdi","ali" ,"najm"]
# result = []
# for name in names:
#     if name[0] == "a":
#         result.append(name.upper())
# print(result)

# resul = [name.upper() for name in names if name.startswith("a")]
# print(resul)
# email_address = []
# for name in names:
#     email = name + "@gmail.com"
#     email_address.append(email)
# print(email_address)

name = "abdi"
nami = [name.upper() for name in name]
print(nami)

names = ["abdi","ali" ,"najm"]
email = [name + "@gmail.com" for name in names]
print(email)

scores = [12,20,30,40,40,10,3,4]
results = []
for score in scores:
    if score > 20:
        results.append("pass")
    else:
        results.append("fail")
print(results)

results = ["pass" if score > 30 else "fail" for score in scores]
print(results)

usd_prices = [100,200,300]
ksh_prices = []

for price in usd_prices:
    ksh_price = price * 100
    ksh_prices.append(ksh_price)
print(ksh_prices)

ksh_prices = [price * 100 for price in usd_prices]
print(ksh_prices)
