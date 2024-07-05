import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()

    
    def display_person_details(self):
        current_year = datetime.date.today().year
        birth_year = self.date_of_birth.year
        age = current_year - birth_year
        print("Name: ", self.name)
        print("Country: ", self.country)
        print("Date of Birth: ",self.date_of_birth)
        print("Current Age: ", age)


obj1 = Person("Nithin", "India", "2000-08-09")
obj1.display_person_details()