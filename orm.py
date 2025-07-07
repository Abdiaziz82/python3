import sqlite3

db_connection = sqlite3.connect('my_database.db')
db_cursor = db_connection.cursor()

class Student:
    def __init__(self,full_name,emailaddress,reg_number):
        self.id = None
        self.full_name = full_name
        self.emailaddress = emailaddress
        self.reg_number = reg_number
        

    def save_attr(self):
        sql = """
        INSERT INTO students(full_name,emailaddress,reg_number) 
         VALUES(? ,? ,?)
        """
        db_cursor.execute(sql ,(self.full_name,self.emailaddress,self.reg_number))
        db_connection.commit()
        self.id = db_cursor.lastrowid    

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            emailaddress TEXT,
            reg_number TEXT
        )
        """
        
        db_cursor.execute(sql)
        db_connection.commit()
        
Student.create_table()
student_1 = Student("abdiaziz" , "abdiazizgmail.com" , "A657877" )
student_2 = Student("amina" , "abdzgmail.com" , "A65juuu7877" )
student_2.save_attr()
print(student_2.id)
        

