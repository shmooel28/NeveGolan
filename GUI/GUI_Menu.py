from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QInputDialog, QLineEdit, QMessageBox, QHBoxLayout, \
    QVBoxLayout, QFormLayout, QTableWidgetItem, QTableWidget, QDialog
from PySide2 import QtWidgets

from GUIEditEvent import GUIEditEvent
from GUIEditEmployee import GUIEditEmployee
from GUIEditStudent import GUIEditStudent
from GUIEmployee import GUIEmployee
from GUIFilterStudent import GUIFilterStudent
from GUIStudent import GUIStudent


def print_error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText('ERROR- cannot find the name')
    x = msg.exec_()


class GUI_Menu(QWidget):
    def __init__(self, algo):
        self.algo = algo
        super().__init__()
        self.title = 'מערכת לניהול נווה גולן - תפריט'
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
        self.setFixedSize(self.width, self.height)

        button = QPushButton('חזרה', self)
        button.setGeometry(40, 40, 200, 200)
        button.move(100, 170)
        button.clicked.connect(self.back)
        button.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button1 = QPushButton('חיפוש חניך', self)
        button1.setGeometry(40, 40, 200, 200)
        button1.move(300, 170)
        button1.clicked.connect(self.search_student)
        button1.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button2 = QPushButton('חיפוש איש צוות', self)
        button2.setGeometry(40, 40, 200, 200)
        button2.move(500, 170)
        button2.clicked.connect(self.search_employee)
        button2.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button3 = QPushButton('סינון', self)
        button3.setGeometry(40, 40, 200, 200)
        button3.move(100, 370)
        button3.clicked.connect(self.filtering)
        button3.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button4 = QPushButton('ערוך סטודנט', self)
        button4.setGeometry(40, 40, 200, 200)
        button4.move(300, 370)
        button4.clicked.connect(self.edit_student)
        button4.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button5 = QPushButton('ערוך איש צוות', self)
        button5.setGeometry(40, 40, 200, 200)
        button5.move(500, 370)
        button5.clicked.connect(self.edit_employee)
        button5.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button6 = QPushButton('ערוך אירוע', self)
        button6.setGeometry(40, 40, 200, 200)
        button6.move(300, 570)
        button6.clicked.connect(self.edit_event)
        button6.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

    @pyqtSlot()
    def edit_event(self):
        event_name, okPressed = QInputDialog.getText(self, "event name", "Enter event name:", QLineEdit.Normal, "")
        if okPressed and event_name != '' and event_name in self.algo.main_system.EVENT:
            self.new_window = GUIEditEvent(self.algo, event_name)
            self.new_window.show()
        else:
            print_error()

    @pyqtSlot()
    def filtering(self):
        self.new_window = GUIFilterStudent(self.algo)
        self.new_window.show()

    @pyqtSlot()
    def edit_student(self):
        first_name, okPressed = QInputDialog.getText(self, "first name", "Enter first name:", QLineEdit.Normal, "")
        if okPressed and first_name != '':
            last_name, okPressed = QInputDialog.getText(self, "first name", "Enter last name:", QLineEdit.Normal, "")
            if okPressed and last_name != '':
                student = self.algo.find_student(first_name, last_name)
                self.edit_s(student)

    @pyqtSlot()
    def edit_employee(self):
        first_name, okPressed = QInputDialog.getText(self, "first name", "Enter first name:", QLineEdit.Normal, "")
        if okPressed and first_name != '':
            last_name, okPressed = QInputDialog.getText(self, "first name", "Enter last name:", QLineEdit.Normal, "")
            if okPressed and last_name != '':
                employee = self.algo.find_employee(first_name, last_name)
                self.edit_e(employee)

    @pyqtSlot()
    def search_student(self):
        first_name, okPressed = QInputDialog.getText(self, "first name", "Enter first name:", QLineEdit.Normal, "")
        if okPressed and first_name != '':
            last_name, okPressed = QInputDialog.getText(self, "first name", "Enter last name:", QLineEdit.Normal, "")
            if okPressed and last_name != '':
                student = self.algo.find_student(first_name, last_name)
                self.show_student(student)

    @pyqtSlot()
    def search_employee(self):
        first_name, okPressed = QInputDialog.getText(self, "first name", "Enter first name:", QLineEdit.Normal, "")
        if okPressed and first_name != '':
            last_name, okPressed = QInputDialog.getText(self, "first name", "Enter last name:", QLineEdit.Normal, "")
            if okPressed and last_name != '':
                employee = self.algo.find_employee(first_name, last_name)
                self.show_employee(employee)

    @pyqtSlot()
    def back(self):
        self.close()

    def show_student(self, student):
        if not student:
            print_error()
        else:
            self.new_window = GUIStudent(self.algo, student)
            self.new_window.show()

    def show_employee(self, employee):
        if not employee:
            print_error()
        else:
            self.new_window = GUIEmployee(employee)
            self.new_window.show()

    def edit_s(self, student):
        if not student:
            print_error()
        else:
            self.new_window = GUIEditStudent(self.algo, student)
            self.new_window.show()

    def edit_e(self, employee):
        if not employee:
            print_error()
        else:
            self.new_window = GUIEditEmployee(employee, self.algo)
            self.new_window.show()
