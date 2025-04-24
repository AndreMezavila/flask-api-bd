from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    room = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Student('{self.name}','{self.email}', '{self.room}')"
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns} 

@app.route('/students', methods=['GET'] )
def list_students_all():
    students = Student.query.all()
    return jsonify([student.as_dict() for student in students])

@app.route('/students/<int:student_id>', methods=['GET'])
def list_student_id(student_id):
  return students.get(
      student_id,
      {'error': 'Student not found'}
  )

@app.route('/students', methods=['POST'])
def create_student():
    id = sorted(students.keys())[-1] +1
    new_student = {
        'name' : request.json['name'],
        'email' : request.json['email'],
        'room' : request.json['room'],
    }
    students[id] = new_student
    return new_student

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    if student_id not in students:
        return {'error': 'Student not found'}, 404

    del students[student_id]
    return {'message': 'Student deleted successfully'}

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    if student_id in students.keys():
        students[student_id]['name']=request.json['name']
        students[student_id]['email']=request.json['email']
        students[student_id]['room']=request.json['room']
        return students[student_id]
    else:
        return {'error': 'student not found'}
