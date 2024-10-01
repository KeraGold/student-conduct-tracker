from App.models import Student, Course
from App.database import db

# Create a new student
def create_student(name, grade, behaviour_status):
    try:
        student = Student (name = name, grade = grade, behaviour_status = behaviour_status)
        db.session.add(student)
        db.session.commit()
        return student
    except Exception as e:
        print(f'Error creating student: {e}')
        db.session.rollback()
        return None

# Get a student by their ID
def get_student_by_id(student_id):
    return Student.query.get(student_id)

# Add a course to a student's list of courses
def add_course_to_student(student_id, course_id):
    student = get_student_by_id(student_id)
    course = Course.query.get(course_id)

    if student and course:
        try:
            student.addCourse(course)
            db.session.commit()
            return True
        except Exception as e:
            print(f'Error adding course to student: {e}')
            db.session.rollback()
            return False
    return False

# Get all students
def get_all_students():
    return Student.query.all()

# Add a review to a student
def add_review_to_student(student_id, review):
    student = get_student_by_id(student_id)
    if student:
        try:
            student.addReview(review)
            db.session.commit()
            return True
        except Exception as e:
            print(f'Error adding review to student: {e}')
            db.session.rollback()
            return False
    return False


# Get all reviews of a student
def get_reviews_of_student(student_id):
    student = get_student_by_id(student_id)
    if student:
        return student.getReviews()
    return []

# Delete a student by ID
def delete_student_by_id(student_id):
    try:
        student = get_student_by_id(student_id)
        if student:
            db.session.delete(student)
            db.session.commit()
            return True
        return False
    except Exception as e:
        print(f'Error deleting student: {e}')
        db.session.rollback()
        return False

