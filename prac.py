class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    @property
    def email(self):
        print('getting email')
        return self._email
    @email.setter
    def email(self,email):
        print('setting email')
        if email.count('@') == 1 :
            self._email = email
        else:
            print("email must contain a")
            self._email = None
        
    @email.deleter
    def email(self):
        print('deleting email')
        del self._email
        
    @property
    def password(self):
        print('getting password')

    def get_password(self):
        print('getting password')
        return self._password
    def set_password(self,password):
        print('setting password')
        if len(password) > 9 :
            self._password = password
            
        else:
            print("password must be longer than 8 characters")
    def delete_password(self):
        print("deleting password")
        del self._password
        
    password = property(get_password, set_password,
                        delete_password, "password")


user_1 = User("Anna", "anna@anna.com", "annagggggf" )
user_3 = User("Anna", "anna@anna.com", "annafrrrrrrr" )
print(user_1.name)
# user_2 = User.__new__(User)
# user_2.__init__("John", "john@john.com", "john123")
# print(user_2.name)
print(user_1.password)

print(user_1.password)
user_1.email = "hhh"

print(getattr(user_1,'password'))
print(user_1.email)


