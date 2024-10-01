from App.database import db
from App.models.student import Student
from App.models.review import Review

class Staff(db.Model):
    __tablename__: 'staff'

    # Attributes (Columns)
    staff_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(125), nullable = False)
    email = db.Column(db.String(125), unique = True, nullable = False)
    role = db.Column(db.String(50), nullable = False)

    # Relationships
    students = db.relationship('Student', secondary = 'review', primaryjoin = "Staff.staff_id == Review.staff_id", viewonly = True, overlaps = "reviews_given, courses")
    reviews = db.relationship('Review', backref = 'staff', lazy = True) 

    # Constructor
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    # Methods
    def addStudent(self, student):
        if student not in self.students:
            self.students.append(student)
    
    def reviewStudent(self, student, review):
        if review not in self.reviews:
            self.reviews.append(review)
        
    def searchStudent(self, criteria):
        # Search students based on criteria (eg. name or behaviour)
        return [student for student in self.students if criteria.lower() in student.name.lower() or criteria.lower() in student.behaviour_status.lower()]
    
    def viewStudentReviews(self, student):
        # Return views for the specified student
        return [review for review in self.reviews if review.student_id == student.student_id]

    # String represenation
    def __repr__(self):
        return f'<Staff: {self.name}, Role: {self.role}>'
    
    # Convert object to JSON
    def toJSON(self):
        return {
            'staffID': self.staff_id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'students': [student.toJSON() for student in self.students],
            'reviews': [review.toJSON() for review in self.reviews]
        }




