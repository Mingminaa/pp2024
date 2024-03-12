import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__marks = {}  # Initialize marks as an empty dictionary

    # Encapsulation part
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

    def get_marks(self):
        return self.__marks

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = math.floor(mark * 10) / 10  

class Course:
    def __init__(self, course_id, course_name, credits):
        self.__id = course_id
        self.__name = course_name
        self.credits = credits
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f" Course ID: {self.__id}\n Course name:{self.__name}\n Credits: {self.credits}"

class Utils:
    # Ask the user to input something
    def input_something(args):
        return int(input(f"Enter the number of {args} in this class: "))

class University:
    def __init__(self):
        # Initialize the list for DATA option
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = {}
        self.__courses = []
        self.__student_gpa = {}  # Initialize the GPA dictionary

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
            self.__students[id] = Student(id, name, dob)

    def set_courses(self):
        num_courses = self.get_num_courses()
        for _ in range(num_courses):
            course_id = input("Enter course id: ")
            course_name = input("Enter course name: ")
            credits = int(input("Enter credits for the course: "))
            self.__courses.append(Course(course_id, course_name, credits))

    # Input the student mark in a course based on the course id
    def input_mark(self):
        course_id = input("Enter the course id: ")
        if course_id not in [course.get_id() for course in self.__courses]:
            print("Invalid course id")
            return
        student_id = input("Enter student id: ")
        student = self.__students.get(student_id)
        if student is None:
            print("Student not found!")
            return
        mark = float(input(f"Enter mark of {student.get_name()} for the course: "))
        student.add_mark(course_id, mark)

    # Display a list of students with marks
    def list_students(self):
        if len(self.__students) == 0:
            print("There aren't any students yet")
        else:
            print("Here is the student list: ")
            for student_id, student in self.__students.items():
                print(f"{student.get_id()} - {student.get_name()} - {student.get_dob()}")
                if student.get_marks():
                    print("Marks (Course Id - Mark): ", end="")
                    for course_id, mark in student.get_marks().items():
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
        for student_id, student in self.__students.items():
            if student.get_id() == student_id:
                course_id = input("Enter course id: ")
                if student.get_marks() and course_id in student.get_marks():
                    print(f"Mark for {course_id}: {student.get_marks()[course_id]}")
                else:
                    print(f"No mark found in that course {course_id}")
                break
        else:
            print("Student not found!")

    # Function to calculate average gpa for a given student
    def calculate_gpa(self, student_id):
        student = self.__students.get(student_id)
        if student is None:
            return None
        if student.get_marks():
            total_credits = 0
            weighted_sum = 0
            for course_id, mark in student.get_marks().items():
                matching_courses = [course for course in self.__courses if course.get_id() == course_id]
                if matching_courses:
                    credits = matching_courses[0].credits
                    total_credits += credits
                    weighted_sum += mark * credits
            if total_credits == 0:
                return 0
            return weighted_sum / total_credits
        else:
            return 0
        
    #Function to sort students by gpa
    def sort_students_by_gpa(self):
        for student_id, student in self.__students.items():
            gpa = self.calculate_gpa(student_id)
            if gpa is not None:
                self.__student_gpa[student] = gpa
        sorted_students = sorted(self.__student_gpa.items(), key=lambda x: x[1], reverse=True)
        for student, gpa in sorted_students:
            print(f"{student.get_name()}\n GPA: {gpa:.2f}\n")

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
    5. Sort students by their GPA:
    """) 
        option = int(input("Your choice: "))                                                         # Choose option from 0 -> n
        if option == 0:
            break
        elif option == 1:                                                                            # Option 1
            univ.input_mark()
        elif option == 2:                                                                            # Option 2                                                     
            univ.list_courses()
        elif option == 3:
            univ.list_students()
        elif option == 4:                                                                            # Option n
            univ.show_mark()
        elif option == 5:
            univ.sort_students_by_gpa()
        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()
