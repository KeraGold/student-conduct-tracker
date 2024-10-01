import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Course, Staff, Student, Review
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, 
create_course, get_all_courses_json, create_staff, create_student, log_review)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Course Commands
'''
course_cli = AppGroup('course', help='Course object commands')

@course_cli.command("create", help="Creates a course")
@click.argument("staff_id")
@click.argument("course_code")
@click.argument("course_name")
def create_course_command(staff_id, course_code, course_name):
    create_course(staff_id, course_code, course_name)
    print(f'Course {course_code} created!')

@course_cli.command("list", help="Lists all courses")
@click.argument("format", default="string")
def list_course_command(format):
    if format == 'json':
        print(get_all_courses_json())
    else:
        print(get_all_courses())

app.cli.add_command(course_cli)

'''
Staff Commands
'''
staff_cli = AppGroup('staff', help='Staff object commands')

@staff_cli.command("create", help="Creates a staff member")
@click.argument("name")
@click.argument("email")
@click.argument("role")
def create_staff_command(name, email, role):
    create_staff(name, email, role)
    print(f'Staff member {name} created!')

app.cli.add_command(staff_cli)

'''
Student Commands
'''
student_cli = AppGroup('student', help='Student object commands')

@student_cli.command("create", help="Creates a student")
@click.argument("name")
@click.argument("grade")
@click.argument("behaviour_status")
def create_student_command(name, grade, behaviour_status):
    create_student(name, grade, behaviour_status)
    print(f'Student {name} created!')

app.cli.add_command(student_cli)

'''
Review Commands
'''
review_cli = AppGroup('review', help='Review object commands')

@review_cli.command("create", help="Creates a review")
@click.argument("staff_id")
@click.argument("student_id")
@click.argument("type")
@click.argument("details")
@click.argument("course_id")
def create_review_command(staff_id, student_id, type, details, course_id):
    create_review(staff_id, student_id, type, details, course_id)
    print(f'Review for student {student_id} created!')

app.cli.add_command(review_cli)

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)