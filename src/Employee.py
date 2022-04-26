from src.Person import Person


class Employee(Person):
    def __init__(self, first_name, last_name, id, gender, age, speciality, phone_number, experience=0, salary=0):
        super().__init__(first_name, last_name, id,gender, age,phone_number)
        self.speciality = speciality
        self.experience = experience
        self.salary = salary
        self.days = ""

    def update_salary(self,salary):
        self.salary = salary

    def update_experience(self,experience):
        self.experience = experience
