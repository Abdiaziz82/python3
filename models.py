from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData 

# Define naming convention for database
# constraints to ensure consistent naming
metadata = MetaData(naming_convention= {
    "pk":"pk_%(table_name)s",  # Primary key 
    "fk" : "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"  # Foreign key 
})
#initialize SQLAlchemy instance
db = SQLAlchemy(metadata= metadata)

class Student(db.Model):
    __tablename__ = 'students'
    #column fields
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100) ,nullable = False)  
    email = db.Column(db.String(50) , unique = True)       
    reg_number = db.Column(db.String ,nullable = False,unique = True)     
    course = db.Column(db.String)  
    school = db.Column(db.String)       
    department = db.Column(db.String(30))  
    
    payment = db.relationship('Payment_history',backref = 'student')
    

    def __repr__(self):
        return f"< Student {self.full_name} >"
    
class Payment_history(db.Model):  
    __tablename__ = 'payments_history'
    id = db.Column(db.Integer, primary_key = True) 
    amount_paid = db.Column(db.Integer ,nullable = False )
    balance = db.Column(db.Integer ,nullable = False)
    method = db.Column(db.String(40) , nullable = False)
    receipt = db.Column(db.Integer , nullable = False)
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))


    