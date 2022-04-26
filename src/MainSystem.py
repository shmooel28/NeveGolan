from src.Employee import Employee
from src.Event import Event
from src.Student import Student


class MainSystem:
    def __init__(self):
        self.employees = {}
        self.students = {}
        self.EVENT = {}
        self.count_student = 0
        self.count_employee = 0
        self.count_event = 0
        self.link = []

    def add_event(self, event: Event):
        self.EVENT[event.event_name] = event
        self.count_event +=1

    def remove_event(self,event):
        if event in self.EVENT:
            self.EVENT.pop(event.event_name)
            self.count_event -= 1

    def add_student(self, student: Student):
        self.students[student._id] = student
        self.count_student += 1

    def add_employee(self, employee: Employee):
        self.employees[employee._id] = employee
        self.count_employee += 1

    def remove_student(self, student):
        try:
            self.students.pop(student._id)
            self.count_student -= 1
            return True
        except KeyError:
            return False

    def remove_employee(self, employee):
        try:
            self.employees.pop(employee._id)
            self.count_employee -= 1
            return True
        except KeyError:
            return False

    def get_all_student(self):
        return self.students

    def get_all_employee(self):
        return self.employees