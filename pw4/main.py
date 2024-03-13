from domains import University
from input import set_students, set_courses, input_mark
from output import list_students, list_courses, show_mark, sort_students_by_gpa

def main():
    univ = University()
    univ.set_num_students()
    set_students(univ)
    univ.set_num_courses()
    set_courses(univ)

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
            input_mark(univ)
        elif option == 2:                                                                            # Option 2                                                     
            list_courses(univ)
        elif option == 3:
            list_students(univ)
        elif option == 4:                                                                            # Option n
            show_mark(univ)
        elif option == 5:
            sort_students_by_gpa(univ)
        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()