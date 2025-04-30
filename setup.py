from app import app, db, Student
app.app_context().push()
db.create_all()
Student.query.all()


student1 = Student(name='John Doe',email='johndoe@exemple.com', room='A101')
student2 = Student(name='Jane Smith',email='janesmith@exemple.com', room='A102')

db.session.add(student1)
db.session.add(student2)
db.session.commit()

students = Student.query.all()
for student in students:
    print(student.id, student.name, student.email, student.room)