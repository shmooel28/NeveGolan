import sys
from datetime import date

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QLineEdit, QVBoxLayout, \
    QMessageBox, QTableWidget, QScrollBar, QTableWidgetItem, QCalendarWidget, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QPoint

from GUIEvent import GUIEvent
from GUIStudent import GUIStudent
from GUIEmployee import GUIEmployee
from GUI_Menu import GUI_Menu
from GUIFile import GUIFile

from src.Algo import Algo
from src.Employee import Employee
from src.Event import Event
from src.Student import Student


class App(QWidget):

    def __init__(self, algo):
        self.algo = algo
        super().__init__()
        self.title = 'מערכת לניהול נווה גולן'
        self.left = 0
        self.top = 0
        self.width = 1280
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel(self)
        pixmap = QPixmap('background1.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.setWindowIcon(QIcon("tel-aviv-logo.jpeg"))
        self.setFixedSize(self.width, self.height)

        button1 = QPushButton('רשימת אנשי צוות', self)
        button1.setGeometry(40, 40, 200, 200)
        button1.move(100, 170)
        button1.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button1.clicked.connect(self.show_employee)

        button2 = QPushButton('רשימת חניכים', self)
        button2.setGeometry(40, 40, 200, 200)
        button2.move(300, 170)
        button2.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button2.clicked.connect(self.show_student)

        button3 = QPushButton('הוסף חניך', self)
        button3.setGeometry(40, 40, 200, 200)
        button3.move(500, 170)
        button3.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button3.clicked.connect(self.add_student)

        button4 = QPushButton('save', self)
        button4.setGeometry(40, 40, 200, 200)
        button4.move(100, 370)
        button4.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button4.clicked.connect(self.save)

        button5 = QPushButton('הוסף איש צוות', self)
        button5.setGeometry(40, 40, 200, 200)
        button5.move(500, 370)
        button5.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button5.clicked.connect(self.add_employee)

        button6 = QPushButton('תפריט', self)
        button6.setGeometry(40, 40, 200, 200)
        button6.move(300, 370)
        button6.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button6.clicked.connect(self.menu)

        button7 = QPushButton('אירועים', self)
        button7.setGeometry(40, 40, 200, 200)
        button7.move(300, 570)
        button7.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button7.clicked.connect(self.show_event)

        button8 = QPushButton('הוסף אירוע', self)
        button8.setGeometry(40, 40, 200, 200)
        button8.move(500, 570)
        button8.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button8.clicked.connect(self.add_event)

        button9 = QPushButton('לוח שנה', self)
        button9.setGeometry(40, 40, 200, 200)
        button9.move(100, 570)
        button9.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                              u";\nborder-radius:10;\nborder-color:black;")
        button9.clicked.connect(self.calander)

        button10 = QPushButton('קבצים', self)
        button10.setGeometry(40, 40, 200, 200)
        button10.move(700, 170)
        button10.setStyleSheet(u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
                               u";\nborder-radius:10;\nborder-color:black;")
        button10.clicked.connect(self.file)

        self.show()

    @pyqtSlot()
    def file(self):
        self.new_window = GUIFile(self.algo)
        self.new_window.show()

    @pyqtSlot()
    def add_event(self):
        event_name = self.get_event_name()
        date = self.get_date()
        if date and event_name:
            temp_event = Event(event_name, date)
            self.algo.main_system.add_event(temp_event)
            self.algo.main_system.task[date.strftime("%d-%m-%Y")] = event_name

    @pyqtSlot()
    def show_event(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.algo.main_system.count_event + 1)
        self.tableWidget.setColumnCount(3)
        self.sqrul = QScrollBar()
        self.tableWidget.setVerticalScrollBar(self.sqrul)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("number"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("event name"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("date"))
        # self.tableWidget.setItem(0, 3, QTableWidgetItem("phone number"))
        self.tableWidget.move(0, 0)
        count = 1

        for e in self.algo.main_system.EVENT:
            da = str(self.algo.main_system.EVENT[e].date.year) + '-' + str(
                self.algo.main_system.EVENT[e].date.month) + '-' + str(self.algo.main_system.EVENT[e].date.day)
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(count)))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(self.algo.main_system.EVENT[e].event_name))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(da))
            count += 1
        self.tableWidget.doubleClicked.connect(self.event_doubleClicked)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)

        self.back_b = QPushButton()
        self.back_b.setText('חזרה')
        self.back_b.clicked.connect(self.back_to_main)
        self.layout.addWidget(self.back_b)

        self.setLayout(self.layout)

        self.show()

    @pyqtSlot()
    def menu(self):
        self.new_window = GUI_Menu(self.algo)
        self.new_window.show()

    @pyqtSlot()
    def add_employee(self):
        first_name = self.get_first_name()
        last_name = self.get_last_name()
        id = self.get_id()
        gender = self.get_gender()
        age = self.get_age()
        phone_number = self.get_phone_number()
        speciality = self.get_speciality()
        if first_name and last_name and gender and age and speciality and phone_number:
            temp_employee = Employee(first_name, last_name, id, gender, age, speciality, phone_number)
            self.algo.main_system.add_employee(temp_employee)

    @pyqtSlot()
    def save(self):
        if self.algo.save_to_json('demo.json'):
            msg = QMessageBox()
            msg.setText("נשמר בהצלחה!!")

            x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('ERROR')

            x = msg.exec_()

    @pyqtSlot()
    def show_employee(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.algo.main_system.count_employee + 1)
        self.tableWidget.setColumnCount(4)
        self.sqrul = QScrollBar()
        self.tableWidget.setVerticalScrollBar(self.sqrul)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("number"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("first name"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("last name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("phone number"))
        self.tableWidget.move(0, 0)
        count = 1
        for e in self.algo.main_system.employees:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(count)))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(self.algo.main_system.employees[e].first_name))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(self.algo.main_system.employees[e].last_name))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(self.algo.main_system.employees[e].phone_number))
            count += 1
        self.tableWidget.doubleClicked.connect(self.employee_doubleClicked)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)

        self.back_b = QPushButton()
        self.back_b.setText('חזרה')
        self.back_b.clicked.connect(self.back_to_main)
        self.layout.addWidget(self.back_b)

        self.setLayout(self.layout)

        self.show()

    @pyqtSlot()
    def back_to_main(self):
        self.cams = App(self.algo)
        self.cams.show()
        self.close()

    @pyqtSlot()
    def show_student(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.algo.main_system.count_student + 1)
        self.tableWidget.setColumnCount(4)
        self.sqrul = QScrollBar()
        self.tableWidget.setVerticalScrollBar(self.sqrul)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("number"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("first name"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("last name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("phone number"))
        self.tableWidget.move(0, 0)
        count = 1
        for s in self.algo.main_system.students:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(count)))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(self.algo.main_system.students[s].first_name))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(self.algo.main_system.students[s].last_name))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(self.algo.main_system.students[s].phone_number))
            count += 1

        self.tableWidget.doubleClicked.connect(self.student_doubleClicked)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)

        self.back_b = QPushButton()
        self.back_b.setText('חזרה')
        self.back_b.clicked.connect(self.back_to_main)
        self.layout.addWidget(self.back_b)

        self.setLayout(self.layout)

    @pyqtSlot()
    def student_doubleClicked(self):
        first_name = self.tableWidget.currentIndex().siblingAtColumn(1).data()
        last_name = self.tableWidget.currentIndex().siblingAtColumn(2).data()
        student = self.algo.find_student(first_name, last_name)
        self.new_window = GUIStudent(self.algo, student)
        self.new_window.show()

    @pyqtSlot()
    def event_doubleClicked(self):
        event_name = self.tableWidget.currentIndex().siblingAtColumn(1).data()
        event = self.algo.main_system.EVENT[event_name]
        self.new_window = GUIEvent(event)
        self.new_window.show()

    @pyqtSlot()
    def employee_doubleClicked(self):
        first_name = self.tableWidget.currentIndex().siblingAtColumn(1).data()
        last_name = self.tableWidget.currentIndex().siblingAtColumn(2).data()
        employee = self.algo.find_employee(first_name, last_name)
        self.new_window = GUIEmployee(employee)
        self.new_window.show()

    @pyqtSlot()
    def add_student(self):
        first_name = self.get_first_name()
        last_name = self.get_last_name()
        id = self.get_id()
        gender = self.get_gender()
        age = self.get_age()
        grade = self.get_grade()
        phone_number = self.get_phone_number()
        if first_name and last_name and id and gender and age and grade and phone_number:
            temp_Student = Student(first_name, last_name, id, gender, age, grade, phone_number)
            self.algo.main_system.add_student(temp_Student)

    def get_speciality(self):
        text, okPressed = QInputDialog.getText(self, "מקצוע", "הכנס מקצוע:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text
        else:
            return None

    def get_event_name(self):
        text, okPressed = QInputDialog.getText(self, "שם אירוע", "הכנס שם אירוע:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text
        else:
            return None

    def get_date(self):
        i, okPressed1 = QInputDialog.getInt(self, "שנה", "הכנס שנה:", 2022, 0, 2030, 1)
        j, okPressed2 = QInputDialog.getInt(self, "חודש", "הכנס חודש:", 6, 0, 100, 1)
        k, okPressed3 = QInputDialog.getInt(self, "יום", "הכנס יום:", 15, 0, 100, 1)

        if okPressed1 and okPressed2 and okPressed3:
            return date(i, j, k)
        else:
            return None

    def get_first_name(self):
        text, okPressed = QInputDialog.getText(self, "first name", "First name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text
        else:
            return None

    def get_last_name(self):
        text, okPressed = QInputDialog.getText(self, "last name", "last name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text
        else:
            return None

    def get_gender(self):
        text, okPressed = QInputDialog.getText(self, "gender", "enter gender:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text
        else:
            return None

    def get_grade(self):
        text, okPressed = QInputDialog.getText(self, "grade", "enter grade:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text
        else:
            return None

    def get_phone_number(self):
        text, okPressed = QInputDialog.getText(self, "phone number", "enter phone number:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text
        else:
            return None

    def get_id(self):
        i, okPressed = QInputDialog.getText(self, "ID", "enter id:", QLineEdit.Normal, "")
        if okPressed and i != '':
            try:
                return int(i)
            except:
                self.error()
                id = self.get_id()
                return id
        else:
            return None

    def get_age(self):
        i, okPressed = QInputDialog.getInt(self, "age", "enter age:", 18, 0, 100, 1)
        if okPressed:
            return i
        else:
            return None

    @pyqtSlot()
    def calander(self):
        self.wind = QWidget()
        self.wind.resize(850, 450)
        self.textBox = QTextEdit(self.wind)
        self.textBox.setGeometry(0, 0, 300, 350)
        self.textBox.move(500, 0)
        self.save_button = QPushButton(self.wind)
        self.save_button.setGeometry(0, 0, 300, 30)
        self.save_button.move(500, 350)
        self.save_button.setText("save")
        self.save_button.setStyleSheet(u"background-color:yellow;\ncolor:blue;\nborder-radius:10")
        self.layout = QHBoxLayout()
        self.calander_widget = QCalendarWidget(self.wind)
        self.calander_widget.setGeometry(0, 0, 500, 350)
        self.calander_widget.selectionChanged.connect(self.change_date)
        self.save_button.clicked.connect(self.save_task)
        self.layout.addWidget(self.calander_widget)
        self.layout.addWidget(self.textBox)
        if self.calander_widget.selectedDate().toPyDate().strftime("%d-%m-%Y") in self.algo.main_system.task:
            self.textBox.setText(
                self.algo.main_system.task[self.calander_widget.selectedDate().toPyDate().strftime("%d-%m-%Y")])
        else:
            self.textBox.setText(" ")
        for d in self.algo.main_system.task:
            d = str(d)
            dat = d.split('-')
            year = int(dat[2])
            month = int(dat[1])
            day = int(dat[0])
            self.calander_widget.updateCell(date(year,month,day))
        self.wind.show()

    @pyqtSlot()
    def save_task(self):
        self.algo.main_system.task[
            self.calander_widget.selectedDate().toPyDate().strftime("%d-%m-%Y")] = self.textBox.toPlainText()



    @pyqtSlot()
    def change_date(self):
        print(self.calander_widget.selectedDate().toPyDate().strftime("%d-%m-%Y"))
        if self.calander_widget.selectedDate().toPyDate().strftime("%d-%m-%Y") in self.algo.main_system.task:
            self.textBox.setText(
                self.algo.main_system.task[self.calander_widget.selectedDate().toPyDate().strftime("%d-%m-%Y")])
        else:
            self.textBox.setText(" ")

    def error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('ERROR- enter number only')
        x = msg.exec_()


if __name__ == '__main__':
    first_try = Algo()
    first_try.load_from_json("demo.json")
    app = QApplication(sys.argv)
    ex = App(first_try)
    sys.exit(app.exec_())
