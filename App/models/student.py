from App.database import db
from App.models.review import Review

class Student(db.Model):
    __tablename__ = 'student'

    # Attributes (Columns)
    student_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    grade = db.Column(db.String(2), nullable = True)
    behaviour_status = db.Column(db.Text, nullable = True)

    # Relationships 
    courses = db.relationship('Course', secondary = 'course_student', lazy = 'subquery')
    reviews = db.relationship('Review', lazy = 'subquery')

    # Constructor
    def __init__(self, name, grade = None, behaviour_status = None):
        self.name = name
        self.grade = grade
        self.behaviour_status = behaviour_status
    
    # Methods
    def getCourses(self):
        return self.courses

    def addCourse(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def addReview(self, review):
        if review not in self.reviews:
            self.reviews.append(review)

    def updateReview(self, review_id, new_details):
        review = Review.query.get(review_id)
        if review:
            review.details = new_details

    def getReviews(self):
        return self.reviews

    # String represenation
    def __repr__(self):
        return f'<Student: {self.name}, Grade: {self.grade}>'

    # Convert object to JSON
    def toJSON(self):
        return {
            'studentID': self.student_id,
            'name': self.name,
            'grade': self.grade,
            'behaviourStatus': self.behaviour_status,
            'reviews': [reviews.toJSON() for review in self.reviews],
            'courses': [course.toJSON() for course in self.courses]
        }
