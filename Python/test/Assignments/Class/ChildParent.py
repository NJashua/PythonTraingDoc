class Company:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept 
        self.salary = salary

class Employee(Company):
    def __init__(self,name, age, role, dept, salary):
        super().__init__(role, dept, salary)
        self.name = name 
        self.age = age
    
    def show_details(self):
        print(f"Name: {self.name} & Age : {self.age} & Role : {self.role} & Department {self.dept}")


obj1=Employee("nithin", 22, "Intern", "PD", 22000)
obj1.show_details()