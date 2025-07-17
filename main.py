from flask import Flask ,jsonify
from flask_migrate import Migrate
from models import db , Student ,Payment_history

app = Flask(__name__)
# Database configuration - SQLite for development
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Should be boolean, not string

# Initialize migration support
migrate = Migrate(app,db)
db.init_app(app)


# Database setup and sample data creation
with app.app_context():
    db.create_all() 

    student = Student.query.filter_by(full_name = "Khalid abdi").first()
    print(student)
    
    tution_fess = Payment_history(
        amount_paid = 6999,
        balance = 700,
        method = "cash",
        receipt = 5657,
        student_id = 1 
    )
    db.session.add(tution_fess)
    db.session.commit()
    
    # students = Student.query.first()
    # print(students)

    
    # #Sample student 1
    # student_1 = Student(
    #     full_name = "Khalid abdi" ,
    #     email = "khalid@ga.com",
    #     reg_number = "S227/222",
    #     course = "Information Science",
    #     school = "spass",
    #     department = "Computer and information science"
    # )
    
    # # Sample student 2 
    # student_2 = Student(
    #     full_name = "faiza abdi" ,
    #     email = "khalid@ga.com", 
    #     reg_number = "S227/222", 
    #     course = "Information Science",
    #     school = "spass",
    #     department = "Computer and information science"
    # )
    
    # # Add students to database session
    # db.session.add(student_1)
    # db.session.add(student_2)
    
    # # Commit changes to database
    # db.session.commit()
  
@app.route('/')
def display_students():
    students = Student.query.all()
    all_students = "<h1>List of all students in the database</h1>"
    for student in students:
        all_students += f"""
        <p>{student.full_name}</p>
        <p>{student.email}</p>
        <p>{student.reg_number}</p>
        <p>{student.course}</p>
        <p>{student.school}</p>
        <p>{student.department}</p>
        """
    return all_students

@app.route('/student_json')
def student_in_json():
    students = Student.query.all()
    all_students = []
    for student in students:
        all_students.append({
            "full_name": student.full_name,
            "email":student.email,
            "reg_number":student.reg_number,
            "course":student.course,
            "school":student.school,
            "department":student.department
        })
    return jsonify(all_students)
        
    

    
    

     
# Run the application
if __name__ == '__main__':
    app.run(port = 5000 , debug = True)