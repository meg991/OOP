class Person:
    def __init__(self, name, age, program, role): # This is the constructor
        self.name = name
        self.age = age
        self.program = program
        self.role = role
        self.say_hello()
    def say_hello(self):
        print("HELLO :) My name is", self.name, "I am", self.age, "yeard old, enrolled in: ", self.program, "and my role is", self.role)

student_1 = Person("John", 37, "DevOps Course", "Student")
student_2 = Person("Mary", 22, "DevOps Course", "Student")
coordinator_1 = Person("Jane", 34, "DevOps Course", "Coordinator")
Instructor_1 = Person ("Bruce", 35, "DevOps Course", "Instructor")
