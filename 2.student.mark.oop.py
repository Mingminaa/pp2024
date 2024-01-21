class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    # Encapsulation part
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

class Course:
    def __init__(self, course_id, course_name):
        self.__id = course_id
        self.__name = course_name
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

class Utils:
    # Ask the user to input something
    def input_something(args):
        return int(input(f"Enter the number of {args} in this class: "))

class University:
    def __init__(self):
        # Initialize the list for DATA option
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []

    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def set_num_students(self):
        self.__num_students = Utils.input_something("students")            

    def set_num_courses(self):
        self.__num_courses = Utils.input_something("courses")              

    def set_students(self):
        num_students = self.get_num_students()
        for _ in range(num_students):
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student dob: ")
            self.__students.append(Student(id, name, dob))

    def set_courses(self):
        num_courses = self.get_num_courses()
        for _ in range(num_courses):
            course_id = input("Enter course id: ")
            course_name = input("Enter course name: ")
            self.__courses.append(Course(course_id, course_name))

    # Input the student mark in a course base on the course id
    def input_mark(self):
        course_id = input("Enter the course id: ")
        if course_id not in [course.get_id() for course in self.__courses]:
            print("Invalid courses id")
            return
        student_id = input("Enter student id: ")
        for student in self.__students:
            if student.get_id() == student_id:
                mark = float(input(f"Enter mark of {student.get_name()} for the course: "))
                if 'marks' not in student.__dict__:
                    student.__dict__['marks'] = {}   
                student.__dict__['marks'][course_id] = mark
                break
        else:
            print("Student not found!")

    # Display a list of students w marks
    def list_students(self):
        if len(self.__students) == 0:
            print("There aren't any students yet")
        else:
            print("Here is the student list: ")
            for student in self.__students:
                print(f"{student.get_id()} - {student.get_name()} - {student.get_dob()}")
                if 'marks' in student.__dict__:
                    print("Marks (Course Id - Mark): ", end="")
                    for course_id, mark in student.__dict__['marks'].items():
                        print(f"{course_id} - {mark}", end=" ")
                    print()

    # Display a list of courses
    def list_courses(self):
        if len(self.__courses) == 0:
            print("There aren't any courses yet")
        else:
            print("Here is the course list: ")
        for course in self.__courses:
            print(f"{course.get_id()} - {course.get_name()}")
    
    # Show student mark for a given course
    def show_mark(self):
        student_id = input("Enter student id: ")
        for student in self.__students:
            if student.get_id() == student_id:
                course_id = input("Enter course id: ")
                if 'marks' in student.__dict__ and course_id in student.__dict__['marks']:
                    print(f"Mark for {course_id}: {student.__dict__['marks'][course_id]}")
                else:
                    print(f"No mark found in that course {course_id}")
                break
        else:
            print("Student not found!")

def main():
    univ = University()
    univ.set_num_students()
    univ.set_students()
    univ.set_num_courses()
    univ.set_courses()

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
            univ.input_mark()
        elif option == 2:                                                                            # Option 2                                                     
            univ.list_courses()
        elif option == 3:
            univ. list_students()
        elif option == 4:                                                                            # Option n
            univ.show_mark()
        else:
            print("Invalid input. Please try again!")


# Call the main function
if __name__ == "__main__":
    main()