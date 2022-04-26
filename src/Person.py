class Person:
    def __init__(self, first_name, last_name, id, gender, age, phone_number):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self._id = id
        self.age = age
        self.gender = gender


    def update_phone_number(self, phone_number):
        self.phone_number = phone_number

    def update_age(self,age):
        self.age = age
