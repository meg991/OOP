from student import Student
from course import Course


devops = Course("DevOps", 35)
meg = Student("Meg", 991)
jack = Student("Jack", 992)

meg.enrol("DevOps")
jack.enrol("Python")

print("Course:", vars(devops))
print("Student:", vars(meg))
print("Student:", vars(jack))

# department_1 = Department("Developer", 1)
# department_1.add_course("Build")
# print(vars(department_1))
#
# department_2 = Department("Operation", 2)
# department_2.add_course("Monitor")
# print(vars(department_2))
#
# course_1 = Course("IT", 123, 105, "Dev")
# course_1.add_course("")
# print(vars(course_1))



