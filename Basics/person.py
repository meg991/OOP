class Person:
    def __init__(self, name, age, program, role):
        self.name = name
        self.age = age
        self.programe = program
        self.role = role

student_1 = Person("John", 37, "DevOps Course", "Student")
#student_1 is an instance of Person
print(student_1.name)
print(student_1.age)
print(student_1.programe)
print(student_1.role)

student_2 = Person("Mary", 22, "DevOps Course", "Student")
print(student_2.name)
print(student_2.age)
print(student_2.programe)
print(student_2.role)

coordinator_1 = Person("Jane", 34, "DevOps Course", "Coordinator")
print(coordinator_1.name)
print(coordinator_1.age)
print(coordinator_1.programe)
print(coordinator_1.role)

Instructor_1 = Person ("Bruce", 35, "DevOps Course", "Instructor")
print(Instructor_1.name)
print(Instructor_1.age)
print(Instructor_1.programe)
print(Instructor_1.role)