from App.database import db

class Review(db.Model):
    __tablename__ = 'review'

    # Attributes (Columns)
    review_id = db.Column(db.Integer, primary_key=True)  # PK
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))  # FK
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))  # FK
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))  # FK
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., Positive or Negative
    details = db.Column(db.Text, nullable=False)

    # Constructor
    def __init__(self, staff_id, student_id, course_id, date, type, details):
        self.staff_id = staff_id
        self.student_id = student_id
        self.course_id = course_id
        self.date = date
        self.type = type
        self.details = details

    # Methods
    def logReview(self, details, type, student, staff, course):
        self.details = details
        self.type = type
        self.student_id = student.student_id
        self.staff_id = staff.staff_id
        self.course_id = course.course_id

    def editReview(self, review_id, new_details):
        review = Review.query.get(review_id)
        if review:
            review.details = new_details

    def getCourseCode(self):
        return self.course.course_code

    # String representation
    def __repr__(self):
        return f'<Review {self.review_id}, Type: {self.type}>'

    # Convert object to JSON
    def toJSON(self):
        return {
            'reviewID': self.review_id,
            'staffID': self.staff_id,
            'studentID': self.student_id,
            'courseID': self.course_id,
            'date': self.date.strftime('%Y-%m-%d'),
            'type': self.type,
            'details': self.details
        }
