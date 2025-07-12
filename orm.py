import sqlite3
# Database connection 
db_connection = sqlite3.connect('my_database.db')
db_cursor = db_connection.cursor()

class Student:
    
    all_students = []  # Class variable to store all students
    
    def __init__(self, full_name, emailaddress, reg_number):
        self.id = None  # Will be set after saving to database
        self.full_name = full_name 
        self.emailaddress = emailaddress 
        self.reg_number = reg_number
        
    def save_attr(self):
        """Save student instance to database"""
        sql = """
        INSERT INTO students(full_name,emailaddress,reg_number) 
         VALUES(? ,? ,?)
        """
        #the question mark is a placeholder to prevent SQL injection
        db_cursor.execute(sql, (self.full_name, self.emailaddress, self.reg_number))
        db_connection.commit()
        self.id = db_cursor.lastrowid  # Get the auto-generated ID from database

    @classmethod
    def create_table(cls):
        """Create students table if it doesn't exist"""
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
        
    @classmethod
    def get_from_db(cls, row):
        """Create Student instance from database row"""
        student = cls(row[1], row[2], row[3])
        student.id = row[0]  # Set ID from database
        return student
    
    @classmethod
    def get_all_students(cls):
        """Retrieve all students from database"""
        sql = """ 
        SELECT * FROM students
        """
        db_cursor.execute(sql)
        all_rows = db_cursor.fetchall()
        cls.all_students = [cls.get_from_db(row) for row in all_rows]
        return cls.all_students
    
    @classmethod
    def find_by_reg_number(cls, reg_number):
        """Find student by registration number"""
        sql = """
        SELECT * FROM students
        WHERE reg_number = ?
        LIMIT 1
        """
        db_cursor.execute(sql, (reg_number,))
        row = db_cursor.fetchone()
        return cls.get_from_db(row) if row else None  # Handle case where no student found
        
# Initialize database table
Student.create_table()

# Create student instances
student_1 = Student("abdiaziz", "abdiazizgmail.com", "A657877")
student_2 = Student("amina", "abdzgmail.com", "A65juuu7877")

# Save student_2 to database
student_2.save_attr()
print(student_2.id)  # Print auto-generated ID

# Query database directly
db_cursor.execute("SELECT * FROM students")
rows = db_cursor.fetchall()
students = Student.get_from_db(rows[0])  # Fixed: use rows[0] since only one record exists
print(students.full_name)
print(students.id)

# Get all students using class method
all_students = Student.get_all_students()
print(all_students[0].full_name)
print(all_students[0].reg_number)  # Fixed: use index 0 since only one student exists

# Find student by registration number
find = Student.find_by_reg_number("A65juuu7877")
print(find.full_name if find else "Student not found")  # Handle potential None result

# Close database connection when done (best practice)
db_connection.close()