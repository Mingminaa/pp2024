
courses = []
students = []

# Ask the user to input a number of unit (course / student)
def input_something(args):
    return int(input(f"Enter the number of {args} in this class: "))

# Ask the user to enter a list of info for an type
def input_infos(args):
    item = {}
    item ['id'] = input(f"Enter {args} id: ")
    item ['name'] = input(f"Enter {args} name: ")
    if args == 'students':
        item['Dob'] = input(f"Enter {args} dob: ")
    return item

# Input the student mark in a course base on the course id
def input_mark(student, courses):
    course_id = input("Enter the course id: ")
    if course_id not in [course['id'] for course in courses]:
        print("Invalid courses id")
        return
    student_id = input("Enter student id: ")
    for student in students:
        if student['id'] == student_id:
            mark = float(input(f"Enter mark of {student['name']} for the course: "))
            if 'marks' not in student:
                student['marks'] = {}   
            student['marks'][course_id] = mark
            break
    else:
        print("Student not found!")


# Display a list of students
def list_students(students):
    if len(students) == 0:
        print("There aren't any students yet")
    else:
        print("Here is the student list: ")
        for student in students:
            print(f"{student['id']} - {student['name']} - {student['Dob']}")
            if 'marks' in student:
                print("Marks (Course Id - Mark): ", end="")
                for course_id, mark in student['marks'].items():
                    print(f"{course_id} - {mark}", end=" ")
                print()

# Display a list of courses
def list_courses(courses):
    if len(courses) == 0:
        print("There aren't any courses yet")
    else:
        print("Here is the course list: ")
        for course in courses:
            print(f"{course['id']} - {course['name']}")

def main():
    num_student = input_something("students")
    for _ in range(num_student):
        students.append(input_infos("students"))

    num_course = input_something("courses")
    for _ in range(num_course):
        courses.append(input_infos("courses"))

    while(True):
        print("""
    0. Exit
    1. Input mark for a student in the course:
    2. List courses:
    3. List students:
    4. Show student marks for a given course:
    """)
        option = int(input("Your choice: "))                                                         # Choose option from 0 -> n
        if option == 0:
            break
        elif option == 1:                                                                            # Option 1
            input_mark(students, courses)
        elif option == 2:                                                                            # Option 2                                                     
            list_courses(courses)
        elif option == 3:                                                                            # Option n
            list_students(students)
        elif option == 4:
            student_id = input("Enter student id: ")
            for student in students:
                if student['id'] == student_id:
                    course_id = input("Enter course id: ")
                    if 'marks' in student and course_id in student['marks']:
                        print(f"Mark for {course_id}: {student['marks'][course_id]}")
                    else:
                        print(f"No mark found in that course {course_id}")
                    break
            else:
                print("Student not found!")
        else:
            print("Invalid input. Please try again!")

# Call the main function
if __name__ == "__main__":
    main()