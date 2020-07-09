OOP - Object Oriented Programming (Paradigm)

Try to mimic the real world into classes or (objects) by using abstraction. The behavior of a class is represented by attributes and actions are executed by methods.

- Classes (objects)
    - Polymorphism
    - Inheritance
- Members
    - Attributes
    - Methods
    - Messages
    - Local variables
    - Access operators
    - Accessibility
    - Encapsulation
    - Interface
 
Syntax of a class:
class NAME:
    # attributes
    # methods
    # constructor 
    
    Example:
        class Person:
            name = "John"
            age = 37
    
write a few classes that could be used in a system for a school using basic OOP principles:

-First you understand the basic of the requirements
    - You understand a bit of the domain that needs to br represented in classes.
    
  1         2         3
Input -> Process -> Output

What are the inputs?
1. What is the input?
2. What are the processes?
3. What is the expected output?

Person  
    Students
    Instructors
    coordinator
Programs
    Levels
        Lessons
            Exercises
Material
Administration

class person:
    name: "John"
    age: 37
    program: "DevOps course"
    role: "student"
    
class person:
    name: "Mary"
    age: 22
    program: "DevOps course"
    role: "student"
    
class person:
    name: "Jane"
    age: 34
    program: "DevOps course"
    role: "coordinator"

class person:
    name: "Bruce"
    age: 35
    program: "DevOps course"
    role: "Instructor"