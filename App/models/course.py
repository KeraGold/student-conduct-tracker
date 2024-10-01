from App.database import db
from App.models.student import Student
from App.models.course_student import course_student

class Course(db.Model):
    __tablename__ = 'course'

    # Attributes
    course_id = db.Column(db.Integer, primary_key = True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))
    course_code = db.Column(db.String(25), unique = True, nullable = False)
    course_name = db.Column(db.String(150), nullable = False)
    course_description = db.Column(db.Text, nullable = False)

    # Relationship
    students_enrolled = db.relationship('Student', secondary = course_student, overlaps = "courses, students_enrolled")

    # Constructor
    def __init__(self, staff_id, course_id, course_code, course_name, course_description):
        self.staff_id = staff_id
        self.course_code = course_code
        self.course_name = course_name
        self.course_description = course_description
    
    # Methods
    def getCourseCode(self):
        return self.course_code

    def getCourseName(self):
        return self.course_name

    def addStudent(self, student):
        if student not in self.students_enrolled:
            self.students_enrolled.append(student)

    def getStudents(self):
        return self.students_enrolled

    # String representation
    def __repr__repr__(self):
        return f'<Course: {self.course_code}, Name: {self.course_name}>'

    # Convert object to JSON format
    def toJSON(self):
        return {
            "courseID": self.course_id,
            "staffID": self.course_id,
            "courseCode": self.course_code,
            "courseName": self.course_name,
            "courseDescription": self.course_description,
            "studentsEnrolled": [student.student.toJSON() for student in self.getStudents()]   
        }