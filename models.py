from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

meta_data = MetaData(naming_convention={
    "pk": "pk_%(table_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=meta_data)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course = db.Column(db.String, nullable=False)

    
    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, course={self.course})"

