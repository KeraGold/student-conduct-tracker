from App.models import Review, Student, Staff, Course
from App.database import db

# Log a new review
def log_review(staff_id, student_id, course_id, details, review_type, date):
    try:
        review = Review(staff_id=staff_id, student_id=student_id, course_id=course_id, details=details, type=review_type, date=date)
        db.session.add(review)
        db.session.commit()
        return review
    except Exception as e:
        print(f'Error logging review: {e}')
        db.session.rollback()
        return None

# Edit a review's details
def edit_review(review_id, new_details):
    try:
        review = Review.query.get(review_id)
        if review:
            review.editReview(review_id, new_details)
            db.session.commit()
            return review
        return None
    except Exception as e:
        print(f'Error editing review: {e}')
        db.session.rollback()
        return None

# Get all reviews of a student
def get_reviews_of_student(student_id):
    return Review.query.filter_by(student_id=student_id).all()

# Delete a review by ID
def delete_review(review_id):
    try:
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False
    except Exception as e:
        print(f'Error deleting review: {e}')
        db.session.rollback()
        return False



