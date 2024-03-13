from domains import Student, Course, Utils

def set_students(univ):
    num_students = univ.get_num_students()
    for _ in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        univ.get_students()[id] = Student(id, name, dob)

def set_courses(univ):
    num_courses = univ.get_num_courses()
    for _ in range(num_courses):
        course_id = input("Enter course id: ")
        course_name = input("Enter course name: ")
        credits = int(input("Enter credits for the course: "))
        univ.get_courses().append(Course(course_id, course_name, credits))

# Input the student mark in a course based on the course id
def input_mark(univ):
    course_id = input("Enter the course id: ")
    if course_id not in [course.get_id() for course in univ.get_courses()]:
        print("Invalid course id")
        return
    student_id = input("Enter student id: ")
    student = univ.get_students().get(student_id)
    if student is None:
        print("Student not found!")
        return
    mark = float(input(f"Enter mark of {student.get_name()} for the course: "))
    student.add_mark(course_id, mark)
