from student import Student
from student import Department
from student import Course

student_1 = Student("John Rambo", 1)

department_1 = Department("IT", 2)
department_2 = Department("Marketing", 3)
department_3 = Department("Sales", 4)

course_1 = Course("DevOps", 3, department_1)
course_2 = Course("Python", 4, department_1)
course_3 = Course("SEO", 5, department_2)
course_4 = Course("CRM - SalesForce", 6, department_3)

