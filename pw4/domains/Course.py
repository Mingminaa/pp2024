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