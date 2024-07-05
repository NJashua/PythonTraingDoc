class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        print(f"Student name is{self.name} and age is{self.age} with grade {self.grade}")
    
name = input("Enter user name: ")
age = int(input("Enter user age: "))
grade = input("Enter user grade: ")
hey = Student(name, age, grade)