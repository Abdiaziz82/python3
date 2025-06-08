# # #accesing list from other list
# # units = ["OOP", "DSA", "DBMS", "OS"]
# # for index in list(range(len(units))):
# #     print("\t",index ,units[index])

# # elements = [2,"abdiaziz" ,["good"] ,{"age":20}]
# # for element in elements:
# #     print(element)

# # my_dict = {"name":"abdiaziz" , "age":20}
# # print(my_dict.items())

# # i = 0 
# # while i < 3:
# #     i+=1
# #     print(i)
# #while loop - there is no need for a collection to iterate over
# #it is good when you dont have a colllection or dont dont know to iterate over
# #you will set a condition and the code inside it will be executed untill the 
# #condition is no longer true
# #you must initialize a value
# #you must increment 
# i = 10
# while i > 0:
#     print(i)
#     i-=1
# print("Done")

# word = ""
# while word != "quit":
#     word = input("enter")
#     if word != "quit":
#         print(word)
#     else:
#         print('goodbye')
        
# number1 = int(input("Enter a number: "))
# i = 0
# while i <= 10:
#     product = number1 * i
#     print(f"{number1} * {i} = {product}")
    # i+=1
    
#nested while loop

# outer_loop = 1
# while outer_loop <= 3:
#     print(f"outer loop iteration {outer_loop}")
#     inner_loop = 1
#     while inner_loop <= 3:
#         print(f"this is the inner loop iteration {inner_loop}")
#         inner_loop+=1
#     print()
#     outer_loop+=1
    
# i = 1
# while i <=3:
#     j= 1
#     while j<=4:
#         total = i * j
#         print(f"{i}* {j} = {total}")
#         j+=1
#     print()
#     i+=1

# #for loop 
# name = "bidd"
# for nam in name:
#     print(nam)
    
# highest_score = 0 
# runner_upp = 0 
# scores = [1,3,5 ,80,80,90]
# for num in scores:
#     if num > highest_score:
#         runner_upp = highest_score
#         highest_score = num
#     elif num > runner_upp:
#         runner_upp = num
# print(f"The highest score is {highest_score}")
# print(f"The runner up is {runner_upp}")

# total = 0
# for num in range(1,101):
#     total+=num
# print(total)

# for row in range(6):
#     for col in range(6):
#         print("*" * col)
        
numbers = [1,2,3,4,5]
# new_num = []
# filtered_num = []
# for num in numbers:
#     result = num **2 
#     if num % 2 == 0:
#         new_num.append(result)
# print(new_num)
  
new_num =[num **2 for num in numbers if num % 2 == 0]
print(new_num)

usd_prices = [12,23,45,67,7]
# ksh_prices = []
# for price in usd_prices:
#     final = price * 100
#     ksh_prices.append(final)
# print(ksh_prices)
    
new = [price * 100 for price in usd_prices]
print(new)