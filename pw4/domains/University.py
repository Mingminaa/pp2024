import math
from .Utils import Utils

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
