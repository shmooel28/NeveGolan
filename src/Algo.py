
import json
from datetime import date

import xlsxwriter

from src.Employee import Employee
from src.Event import Event
from src.MainSystem import MainSystem
from src.Student import Student


class Algo:
    def __init__(self):
        self.main_system = MainSystem()
        self.temp_student_list = {}
        self.temp_count = 0

    def save_to_json(self, file_name):
        try:
            dict_json = {}
            for e in self.main_system.employees:
                temp = self.main_system.employees[e]
                if "Employees" in dict_json:
                    dict_json["Employees"].append(
                        {"id": temp._id, "gender": temp.gender, "last_name": temp.last_name, "age": temp.age,
                         "phone_number": temp.phone_number,
                         "first_name": temp.first_name, "speciality": temp.speciality, "experience": temp.experience,
                         "salary": temp.salary, "days": temp.days})
                else:
                    dict_json["Employees"] = [
                        {"id": temp._id, "gender": temp.gender, "last_name": temp.last_name, "age": temp.age,
                         "phone_number": temp.phone_number,
                         "first_name": temp.first_name, "speciality": temp.speciality, "experience": temp.experience,
                         "salary": temp.salary, "days": temp.days}]

            for s in self.main_system.students:
                temp = self.main_system.students[s]
                if "Students" in dict_json:
                    dict_json["Students"].append(
                        {"id": temp._id, "gender": temp.gender, "last_name": temp.last_name, "age": temp.age,
                         "phone_number": temp.phone_number,
                         "first_name": temp.first_name, "grade": temp.grade, "classes": temp.classes})
                else:
                    dict_json["Students"] = [
                        {"id": temp._id, "gender": temp.gender, "last_name": temp.last_name, "age": temp.age,
                         "phone_number": temp.phone_number,
                         "first_name": temp.first_name, "grade": temp.grade, "classes": temp.classes}]

            for e in self.main_system.EVENT:
                temp = self.main_system.EVENT[e]
                parti = []
                for p in temp.arrival_confirmation:
                    parti.append({"first name":p[0].first_name, "last name":p[0].last_name,"arrival_confirmation":str(p[1])})
                em = []
                for emp in temp.employee:
                    em.append({"first name":emp.first_name, "last name":emp.last_name})
                if "EVENTS" in dict_json:
                    dict_json["EVENTS"].append(
                        {"event name": temp.event_name, "year": temp.date.year, "month": temp.date.month,
                         "day": temp.date.day, "participants": parti, "employee": em,
                         "comment": temp.comment,
                          "equipment_list": temp.equipment_list})
                else:
                    temp = self.main_system.EVENT[e]
                    parti = []
                    for p in temp.arrival_confirmation:
                        parti.append({"first name": p[0].first_name, "last name": p[0].last_name,
                                      "arrival_confirmation": str(p[1])})
                    em = []
                    for emp in temp.employee:
                        em.append({"first name": emp.first_name, "last name": emp.last_name})
                    dict_json["EVENTS"] = [
                        {"event name": temp.event_name, "year": temp.date.year, "month": temp.date.month,
                         "day": temp.date.day, "participants": parti,
                         "employee": em,
                         "comment": temp.comment,
                         "equipment_list": temp.equipment_list}]
            dict_json["LINK"] = self.main_system.link
            dict_json["Task"] = self.main_system.task
            with open(file_name, "w") as out:
                json.dump(dict_json, out, indent=4)
            return True
        except:
            return False

    def load_from_json(self, file_name):
        try:
            with open(file_name, "r") as f:
                self.main_system = MainSystem()
                j = json.load(f)
                for s in j["Students"]:
                    Id = int(s["id"])
                    first_name = s["first_name"]
                    last_name = s["last_name"]
                    gender = s["gender"]
                    age = int(s["age"])
                    grade = s["grade"]
                    phone_number = s["phone_number"]
                    classes = []
                    for c in s["classes"]:
                        classes.append(c)
                    temp_student = Student(first_name, last_name, Id, gender, age, grade, phone_number, classes)
                    self.main_system.add_student(temp_student)

                for e in j["Employees"]:
                    Id = int(e["id"])
                    first_name = e["first_name"]
                    last_name = e["last_name"]
                    age = int(e["age"])
                    gender = e["gender"]
                    phone_number = e["phone_number"]
                    speciality = e["speciality"]
                    experience = int(e["experience"])
                    salary = float(e["salary"])
                    days = e["days"]
                    temp_employee = Employee(first_name, last_name, Id, gender, age, speciality, phone_number,
                                             experience,
                                             salary)
                    temp_employee.days = days
                    self.main_system.add_employee(temp_employee)
                for e in j["EVENTS"]:
                    event_name = e["event name"]
                    year = int(e["year"])
                    month = int(e["month"])
                    day = int(e["day"])
                    Date = date(year, month, day)
                    arrival_confirmation = []
                    count_p = 0
                    for p in e["participants"]:
                        count_p += 1
                        first_name = p["first name"]
                        last_name = p["last name"]
                        temp_student = self.find_student(first_name,last_name)
                        flag = p["arrival_confirmation"]
                        arrival_confirmation.append((temp_student,flag))
                    employee = []
                    count_e = 0
                    for em in e["employee"]:
                        count_e += 1
                        first_name = em["first name"]
                        last_name = em["last name"]
                        temp_employee = self.find_employee(first_name,last_name)
                        employee.append(temp_employee)
                    comment = e["comment"]
                    #arrival_confirmation = e["arrival_confirmation"]
                    equipment_list = e["equipment_list"]
                    temp_event = Event(event_name, Date)
                    temp_event.employee = employee
                    temp_event.comment = comment
                    temp_event.arrival_confirmation = arrival_confirmation
                    temp_event.equipment_list = equipment_list
                    temp_event.count_employee = count_e
                    temp_event.count_student = count_p
                    self.main_system.add_event(temp_event)
                self.main_system.link = j["LINK"]
                self.main_system.task = j["Task"]
            return True
        except:
            return False

    def find_student(self, first_name, last_name):
        for s in self.main_system.students:
            if self.main_system.students[s].first_name == first_name and self.main_system.students[s].last_name == last_name:
                return self.main_system.students[s]
        return None

    def find_employee(self, first_name, last_name):
        for e in self.main_system.employees:
            if self.main_system.employees[e].first_name == first_name and self.main_system.employees[
                e].last_name == last_name:
                return self.main_system.employees[e]
        return None

    def filter_student(self, from_age, to_age, from_grade, to_grade, gender_flag, gender):
        new_student_dict = {}
        count = 0
        for s in self.main_system.students.values():
            if int(to_age) >= int(s.age) >= int(from_age) and to_grade >= s.grade >= from_grade:
                if gender_flag:
                    if s.gender == gender:
                        new_student_dict[s._id] = s
                        count += 1
                else:
                    new_student_dict[s._id] = s
                    count += 1

        return count, new_student_dict

    def write_to_xlsx(self,filename_out,student_list):
        workbook = xlsxwriter.Workbook(filename_out)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': 1})
        worksheet.write('A1', 'שם משפחה', bold)
        worksheet.write('B1', 'שם פרטי', bold)
        worksheet.write('C1', ' מספר פלאפון', bold)
        out_list = {}
        row = 1
        col = 0
        for student in student_list.values():
            worksheet.write_string(row, col, student.last_name)
            worksheet.write_string(row, col+1, student.first_name)
            worksheet.write_string(row, col+2, student.phone_number)
            row+=1
        workbook.close()

    def up_grade(self):
        for s in self.main_system.students.values():
            if s.grade == 'א':
                s.grade ='ב'
            elif s.grade == 'ב':
                s.grade = 'ג'
            elif s.grade == 'ג':
                s.grade = 'ד'
            elif s.grade == 'ד':
                s.grade = 'ה'
            elif s.grade == 'ה':
                s.grade = 'ו'
            elif s.grade == 'ו':
                s.grade = 'ז'
            elif s.grade == 'ז':
                s.grade = 'ח'
            elif s.grade == 'ח':
                s.grade = 'ט'
            elif s.grade == 'ט':
                s.grade = 'י'
            elif s.grade == 'י':
                s.grade = 'יא'
            elif s.grade == 'יא' or s.grade =='י"א':
                s.grade = 'יב'
            else:
                s.grade = 'בוגרים'

