from datetime import datetime, date


class Event:
    def __init__(self, name, Date):
        self.date = Date
        self.event_name = name
        self.employee = []
        self.comment = ''
        self.arrival_confirmation = []
        self.count_employee = 0
        self.count_student = 0
        self.equipment_list = ''

    def add_participants(self,student):
        self.arrival_confirmation.append((student,"לא אישר הגעה"))
        self.count_student+=1

    def add_employee(self,employee):
        self.employee.append(employee)
        self.count_employee+=1

    def remove_participants(self,student):
        if student in self.arrival_confirmation[0]:
            for i in self.arrival_confirmation:
                if i[0] == student:
                    self.arrival_confirmation.remove(i)
            self.count_student -= 1

    def remove_employee(self,employee):
        if employee in self.employee:
            self.employee.remove(employee)
            self.count_employee -= 1

    def count_down(self):
        d = self.date - date.today()
        return d