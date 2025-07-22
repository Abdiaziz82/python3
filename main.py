from flask import Flask ,jsonify ,make_response ,request
from flask_migrate import Migrate
from models import db , Student ,Payment_history
from flask_cors import CORS

app = Flask(__name__)
# Database configuration - SQLite for development
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
CORS(app)
# Initialize migration support
migrate = Migrate(app,db)
db.init_app(app)

@app.route('/post_student', methods=['POST'])
def post_student():
    data = request.get_json()
    
    new_student = Student(
        full_name = data.get('fullName'),
        reg_number = data.get('regNumber'),
        email = data.get('emailAddress'),
        school = data.get('school'),
        course = data.get('course'),
        department = data.get('department'),   
    )
    
    db.session.add(new_student)
    db.session.commit()
    
    student_dict = {
        "id" : new_student.id,
        "full_name" : new_student.full_name,
        "reg_number" :new_student.reg_number,
        "email" : new_student.email,
        "school" : new_student.school,
        "course" : new_student.course,
        "department" : new_student.department
    }
    
    return(jsonify(student_dict), 201)

@app.route('/delete_student/<int:student_id>' , methods =['DELETE'])
def delete_student(student_id):
    student = Student.query.filter(Student.id == student_id).first()
    if not student:
        return(jsonify({"error" : "there is no student with this id in the database"}), 404)
    db.session.delete(student)
    db.session.commit()
    return(jsonify({"message" :"student deleted successfully"}), 200)
    
    
    







@app.route('/students' ,methods = ['GET'] )
def get_student():
    all_students = []
    for student in Student.query.all():
        students_dict = {
            "id" :student.id,
            "full_name" : student.full_name,
            "email" : student.email,
            "reg_number" : student.reg_number,
            "course" : student.course,
            "school" : student.school,
            "department" : student.department
        }
        all_students.append(students_dict)
    return jsonify(all_students)

@app.route('/students/<int:student_id>',methods = ['GET'])
def get_student_details(student_id):
    student = Student.query.filter(Student.id == student_id).first()
    if not student:
        return(jsonify({"error" : "no student in the database with this id"}), 404)
    student_dict = {
        "id" :student.id,
        "full_name" : student.full_name,
        "email" : student.email,
        "reg_number" : student.reg_number,
        "course" : student.course,
        "school" : student.school,
        "department" : student.department
    }
    
    return(jsonify(student_dict))
    







 





# Database setup and sample data creation
# with app.app_context():
#     # db.create_all() 

#     student = Student.query.filter_by(full_name = "Khalid abdi").first()
#     print(student)
    
#     tution_fess = Payment_history(
#         amount_paid = 6999,
#         balance = 7000,
#         method = "mpesa",
#         receipt = 5657,
#         student_id = 5 
#     )
#     db.session.add(tution_fess)
#     db.session.commit()
    
#     students = Student.query.first()
#     print(students)

    
#     #Sample student 1
#     student_1 = Student(
#         full_name = "Khalid abdi" ,
#         email = "khalid@ga.com",
#         reg_number = "S227/222",
#         course = "Information Science",
#         school = "spass",
#         department = "Computer and information science"
#     )
    
#     # Sample student 2 
#     student_2 = Student(
#         full_name = "faiza abdi" ,
#         email = "khalid@ga.com", 
#         reg_number = "S227/222", 
#         course = "Information Science",
#         school = "spass",
#         department = "Computer and information science"
#     )
    
#     # Add students to database session
#     db.session.add(student_1)
#     db.session.add(student_2)
    
#     # Commit changes to database
#     db.session.commit()


@app.route('/payments/<student_id>')   
def display_payments_by_stud(student_id): 
    payment = Payment_history.query.get(student_id)
    if not payment:
        return "no payment history found",404
    resp_body = f"""
    <p>{payment.amount_paid}</p>
    <p>{payment.balance}</p>
    <p>{payment.method}</p>
    <p>{payment.receipt}</p>
    <p>{payment.student.full_name}</p>
    """
    response = make_response(resp_body)
    response.headers['content-type'] = 'text/html'
    return response
    
    
@app.route('/')
def display_students():
    students = Student.query.all()  # Fetches all students from the database
    all_students = "<h1>List of all students in the database</h1>"  # Initializes HTML string with header
    for student in students:  # Loops through each student
        all_students += f"""
        <p>{student.full_name}</p>
        <p>{student.email}</p>
        <p>{student.reg_number}</p>
        <p>{student.course}</p>
        <p>{student.school}</p>
        <p>{student.department}</p>
        """  
    return all_students  # Returns HTML string to display student list


@app.route('/student_json')
def student_in_json():
    students = Student.query.all()  # Fetches all students from the database
    all_students = []  # Initializes empty list for student data
    for student in students:  # Loops through each student
        all_students.append({  # Creates dictionary for each student
            "full_name": student.full_name,
            "email": student.email,
            "reg_number": student.reg_number,
            "course": student.course,
            "school": student.school,
            "department": student.department
        })
    return jsonify(all_students)  # Returns student data as JSON

    

    
    

     
# Run the application
if __name__ == '__main__':
    app.run(port = 5000 , debug = True)