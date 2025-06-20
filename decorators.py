def add_num(a,b):
    return a + b

add = add_num(2,4)
print(add)

#nested function
def outer_function(name):
    print(f"Hi {name} from the outer_function")
    
    def inner_function():
        print(f"Hi {name} from the inner function")
           
    return inner_function

greet_student = outer_function("abdiaziz")
greet_student()

def my_decorator(my_func):
    #wrapper function
    def wrapper():
        print("this is the first time being called")
        #the function to be decorated
        my_func()
        print("this is the last time being called")
    return wrapper

def func_called():
    print("this is the function being called")

#the decorator taking in the function as arguement    
func_called = my_decorator(func_called)            
func_called()

#another example
is_logged_in = False
#decorator for protecting some pages
def require_login(dec_func):
    def wrapper():
        #authentication logic can be applied here
        #before accessing the protected page
        print("Logging in ...........")
        if is_logged_in:
            dec_func()
        else:
            print("Access denied , you are not authorized")
        
    return wrapper   

#the decorated function
@require_login
def view_dashboard():
    print("accessing the dashboard")
    
@require_login   
def change_password():
    print("changing password")
      
#calling the decorated functions
view_dashboard()
change_password()

#lamda functions - Anonymous function
#lamda parameter:expression
add = lambda a,b: a + b
print(add(2,3))
greet_student = lambda name:f"hello  {name}"
print(greet_student("Mohamed"))

#using lambda function as the key for sorting
products = ["laptop","Shoes","phone","charger","Tv"]
new_products = sorted(products,key = lambda x: x[0].upper())
print(new_products)

#lambda function in filter function
filtered_products = filter(lambda b: 'o' not  in b,products)
print(list(filtered_products))

#Lambda function returned by another function
def add_after(name):
    return lambda n : name + n
add = add_after("abdiaziz")
print(add("........."))





