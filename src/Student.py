from src.Person import Person


class Student(Person):
    def __init__(self, first_name, last_name, id, gender, age, grade, phone_number, classes=None):
        super().__init__(first_name, last_name, id, gender, age, phone_number)
        if classes is None:
            classes = []
        self.grade = grade
        self.classes = classes

    def add_class(self, class_a):
        self.classes.append(class_a)

    def remove_class(self, class_a):
        self.classes.remove(class_a)

    def update_grade(self, grade):
        self.grade = grade

    def __repr__(self):
        return ''+self.first_name + '  ' + self.last_name
