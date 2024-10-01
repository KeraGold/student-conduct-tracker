from App.database import db

# Association Table for Many-to-Many relationship between Course and Student
course_student = db.Table(
    'course_student',
    db.Column('course_id', db.Integer, db.ForeignKey('course.course_id'), primary_key = True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.student_id'), primary_key = True)
)


