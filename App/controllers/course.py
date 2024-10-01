from App.models import Course, Student
from App.database import db

# Function to create a new course
def create_course(course_id, staff_id, course_code, course_name, course_description = None):
    try:
        course = Course(staff_id = staff_id, course_code = course_code, course_name = course_name, course_description = course_description)
        db.session.add(course)
        db.session.commit()
        return course
    except Exception as e:
        print(f'Error creating course: {e}')
        db.session.rollback()
        return None

# Function to return a course by its ID
def get_course_by_id(course_id):
    return Course.query.get(course_id)

# Function to retrieve all courses
def get_all_courses():
    return Course.query.all()

# Function to retrieve courses by staff ID
def get_courses_by_staff(staff_id):
    return Course.query.filter_by(staff_id = staff_id).all()

# Function to add a student to a course
def add_student_to_course(course_id, student_id):
    course = get_course_by_id(course_id)
    student = Student.query.get(student_id)

    if course and student:
        try:
            course.addStudent(student)
            db.session.commit()
            return True
        except Exception as e:
            print(f'Error adding student to course: {e}')
            db.session.rollback()
            return False
        return False

# Function to retrieve students enrolled in a specific course
def get_students_in_course(course_id):
    course = get_course_by_id(course_id)
    if course:
        return course.getStudents()
    return None

# Function to delete a course by its ID
def delete_course(course_id):
    try:
        course = get_course_by_id(course_id)
        if course:
            db.session.delete(course)
            db.session.commit()
            return True
        return False
    except Exception as e:
        print(f'Error deleting course: {e}')
        db.session.rollback()
        return False

def get_all_courses_json():
    courses = Course.query.all()
    return [course.to_dict() for course in courses]

def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_code': self.course_code,
            'course_name': self.course_name,
            'course_description': self.course_description
        }
        