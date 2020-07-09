class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.courses = []
    def enrol(self, course):
        self.courses.append(course)

class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}
    def add_course(self, course):
        self.courses[course.course_code] = course
        return self.courses[course.course_code]



#
# class CourseRunning:
#     def __init__(self, course, year):
#         self.course = course
#         self.year = year
#         self.students = []
#     def add_student(self, student):
#         self.students.append(student)
