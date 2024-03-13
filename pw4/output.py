from domains import Student

# Display a list of students with marks
def list_students(univ):
    students = univ.get_students()
    if len(students) == 0:
        print("There aren't any students yet")
    else:
        print("Here is the student list: ")
        for student_id, student in students.items():
            print(f"{student.get_id()} - {student.get_name()} - {student.get_dob()}")
            if student.get_marks():
                print("Marks (Course Id - Mark): ", end="")
                for course_id, mark in student.get_marks().items():
                    print(f"{course_id} - {mark}", end=" ")
                print()

# Display a list of courses
def list_courses(univ):
    courses = univ.get_courses()
    if len(courses) == 0:
        print("There aren't any courses yet")
    else:
        print("Here is the course list: ")
        for course in courses:
            print(f"{course.get_id()} - {course.get_name()}")

# Show student mark for a given course
def show_mark(univ):
    student_id = input("Enter student id: ")
    students = univ.get_students()
    student = students.get(student_id)
    if student is not None:
        course_id = input("Enter course id: ")
        marks = student.get_marks()
        if marks and course_id in marks:
            print(f"Mark for {course_id}: {marks[course_id]}")
        else:
            print(f"No mark found in that course {course_id}")
    else:
        print("Student not found!")

#Function to sort students by gpa
def sort_students_by_gpa(univ):
    univ.sort_students_by_gpa()
