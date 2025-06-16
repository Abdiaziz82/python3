class User:
    def __init__(self, name ,email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    # a "getter" that runs when you access the attribute.
    @property
    def phone_number(self):
        "this is a protected phone number"
        print("getting phone number")
        return self._phone_number

    #  "setter" that runs when you assign a value to the attribute.
    @phone_number.setter
    def phone_number(self , phone_number):
        print("setting_phone_number")
        if phone_number.startswith("+254") and len(phone_number) > 10:
            self._phone_number = phone_number
        else:
            self._phone_number = "not settted"
            print("not set")

    # Creates a "deleter" that runs when you use 'del' on the attribute.
    @phone_number.deleter
    def phone_number(self):
        print("deleting phonenumber")
        del self._phone_number

    def __repr__(self):
        return f"{self.name} {self.email} {self.phone_number}"


user_1 = User("abdullahi" , "abdullahi@gmail" , "+2571234567")
print(user_1)
user_1.name = "ali"
user_1.phone_number = "871234567"
print(user_1.phone_number) # < getting phone number || not settted >
del user_1.phone_number # < deleting phonenumber >
help(User.phone_number) # <this is a protected phone number>
print(User.phone_number.__doc__) # <this is a protected phone number>