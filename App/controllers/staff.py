from App.models import Staff, Student, Review
from App.database import db

# Create a new staff member
def create_staff(name, email, role):
    try: 
        staff = Staff(name = name, email = email, role = role)
        db.session.add(staff) 
        db.session.commit()
        return staff
    except Exception as e:
        print(f'Error creating staff: {e}')
        db.session.rollback()
        return None

# Get a staff member by their ID
def get_staff_by_id(staff_id):
    return Staff.query.get(staff_id)

# Add a student to a staff's list of  students
def add_student_to_staff(staff_id, student_id):
    staff = get_staff_by_id(staff_id)
    student = Student.query.get(student_id)

    if staff and student:
        try:
            staff.addStudent(student)
            db.session.commit()
            return True
        except Exception as e:
            print(f'Error adding student to staff: {e}')
            db,session,rollback()
            return False
    return False

# Review a student
def review_student(staff_id, student_id, review_details, review_type, course_id, date):
    staff = get_staff_by_id(staff_id)
    student = Student.query.get(student_id)

    if staff and student:
        try: 
            review = Review(staff_id = staff_id, student_id = student_id, course_id = course_id, details = review_details, type = review_type, date = date)
            staff.reviewStudent(student, review)
            db.session.add(review)
            db.session.commit()
            return review
        except Exception as e:
            print(f'Error reviewing student: {e}')
            db,session,rollback()
            return None
    return None

# Search for students based on criteria
def search_students_by_criteria(staff_id, criteria):
    staff = get_staff_by_id(staff_staff_id)
    if staff:
        return staff.searchStudent(criteria)
    return []

# View all reviews for a specific student by a staff member
def view_student_reviews(staff_id, student_id):
    staff = get_staff_by_id(staff_id)
    if staff:
        student = Student,query,get(student_id)
        if student:
            return staff.staff.viewStudentReviews(student)
    return []