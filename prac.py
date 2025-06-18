# def my_decorator(func):
#     def wrapper():
#         print("i want")
#         func()
#         print("yow")
#     return wrapper
# def login():
#     print("hhh")
# login = my_decorator(login)
# print(login())
def require_login(func):
    def wrapper():
        print("i am ")
        func()
    return wrapper

@require_login
def login():
    print('user logging in')
login()
a = lambda x,y: x + y
print(a(1,2))

def num(a,b):
    return lambda a,b : a ** b
print(num(2,2))
