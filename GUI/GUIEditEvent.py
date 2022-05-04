from PyQt5.QtCore import pyqtSlot, Qt, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QDialog, QCheckBox, QInputDialog, QVBoxLayout, \
    QDialogButtonBox, QTextEdit, QLineEdit, QTableWidget, QScrollBar, QTableWidgetItem, QRadioButton

from GUIFilterStudent import GUIFilterStudent


class GUIEditEvent(QWidget):
    def __init__(self, algo, event_name):
        self.algo = algo
        self.event_name = event_name
        super().__init__()
        self.title = 'מערכת לניהול נווה גולן - אירועים'
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


        button1 = QPushButton('חזרה', self)
        button1.setGeometry(40, 40, 200, 200)
        button1.move(100, 170)
        button1.clicked.connect(self.back)
        button1.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button2 = QPushButton('הוסף משתתף', self)
        button2.setGeometry(40, 40, 200, 200)
        button2.move(300, 170)
        button2.clicked.connect(self.add_participants)
        button2.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button3 = QPushButton('ערוך אישורי הגעה', self)
        button3.setGeometry(40, 40, 200, 200)
        button3.move(500, 170)
        button3.clicked.connect(self.edit_arrival_confirmation)
        button3.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button4 = QPushButton('הוסף הערה', self)
        button4.setGeometry(40, 40, 200, 200)
        button4.move(100, 370)
        button4.clicked.connect(self.add_comment)
        button4.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button5 = QPushButton('רשימת  ציוד', self)
        button5.setGeometry(40, 40, 200, 200)
        button5.move(300, 370)
        button5.clicked.connect(self.equipment_list)
        button5.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

        button6 = QPushButton('מחיקת אירוע', self)
        button6.setGeometry(40, 40, 200, 200)
        button6.move(500, 370)
        button6.clicked.connect(self.delete_event)
        button6.setStyleSheet(
            u"background-color:rgb(255, 243, 231);\ncolor:black;\nborder-style:outset;\nborder-width:2px"
            u";\nborder-radius:10;\nborder-color:black;")

    @pyqtSlot()
    def back(self):
        self.close()

    @pyqtSlot()
    def add_participants(self):
        self.checkBox1 = QCheckBox()
        self.checkBox1.setText("איש צוות")
        self.checkBox2 = QCheckBox()
        self.checkBox2.setText("חניך")
        self.checkBox4 = QCheckBox()
        self.checkBox4.setText("כל אנשי הצוות")
        self.checkBox5 = QCheckBox()
        self.checkBox5.setText("קבוצת חניכים")
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.cancle)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.checkBox1)
        self.layout.addWidget(self.checkBox2)
        self.layout.addWidget(self.checkBox4)
        self.layout.addWidget(self.checkBox5)
        self.layout.addWidget(self.buttonBox)
        self.wind = QDialog()
        self.wind.setGeometry(70, 70, 200, 200)
        self.wind.setLayout(self.layout)
        self.wind.show()

    @pyqtSlot()
    def cancle(self):
        self.wind.close()

    @pyqtSlot()
    def ok(self):
        if self.checkBox1.isChecked():
            first_name, last_name = self.get_name()
            if first_name and last_name:
                temp_employee = self.algo.find_employee(first_name, last_name)
                if temp_employee:
                    self.algo.main_system.EVENT[self.event_name].add_employee(temp_employee)
        elif self.checkBox2.isChecked():
            first_name, last_name = self.get_name()
            if first_name and last_name:
                temp_student = self.algo.find_student(first_name, last_name)
                if temp_student:
                    self.algo.main_system.EVENT[self.event_name].add_participants(temp_student)
        elif self.checkBox4.isChecked():
            for employee in self.algo.main_system.employees.values():
                if employee not in self.algo.main_system.EVENT[self.event_name].employee:
                    self.algo.main_system.EVENT[self.event_name].add_employee(employee)
        elif self.checkBox5.isChecked():
            self.new_window = GUIFilterStudent(self.algo,self.event_name)
            self.new_window.show()


        self.wind.close()

    @pyqtSlot()
    def edit_arrival_confirmation(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.algo.main_system.EVENT[self.event_name].count_student + 1)
        self.tableWidget.setColumnCount(4)
        self.sqrul = QScrollBar()
        self.tableWidget.setVerticalScrollBar(self.sqrul)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("number"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("first name"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("last name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("אישורי הגעה"))

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.ok_arrival)
        self.buttonBox.rejected.connect(self.back)
        # self.checkBox3 = QCheckBox()
        self.checkBox3 = QCheckBox()
        # self.tableWidget.setItem(0, 3,self.checkBox3)
        # self.tableWidget.setCellWidget()
        self.tableWidget.move(0, 0)
        count = 1

        for student in self.algo.main_system.EVENT[self.event_name].arrival_confirmation:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(count)))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(student[0].first_name))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(student[0].last_name))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(student[1]))
            count += 1
        self.tableWidget.doubleClicked.connect(self.arrival_doubleClicked)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.buttonBox)
        self.back_b = QPushButton()
        self.back_b.clicked.connect(self.back)
        self.back_b.setText('חזרה')

        # self.back_b.clicked.connect(self.back_to_main)
        self.layout.addWidget(self.back_b)

        self.setLayout(self.layout)

        self.show()

    @pyqtSlot()
    def add_comment(self):
        self.wind = QDialog()
        self.textLine = QTextEdit()
        self.textLine.setText(self.algo.main_system.EVENT[self.event_name].comment)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.ok_com)
        self.buttonBox.rejected.connect(self.cancle)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textLine)
        self.layout.addWidget(self.buttonBox)
        self.wind.setLayout(self.layout)
        self.wind.show()

    @pyqtSlot()
    def ok_com(self):
        self.algo.main_system.EVENT[self.event_name].comment = self.textLine.toPlainText()
        self.wind.close()

    @pyqtSlot()
    def equipment_list(self):
        self.wind = QDialog()
        self.textLine = QTextEdit()
        self.textLine.setText(self.algo.main_system.EVENT[self.event_name].comment)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.ok_equipment_list)
        self.buttonBox.rejected.connect(self.cancle)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textLine)
        self.layout.addWidget(self.buttonBox)
        self.wind.setLayout(self.layout)
        self.wind.show()

    def get_name(self):
        first_name, okPressed1 = QInputDialog.getText(self, "first name", "First name:", QLineEdit.Normal, "")
        last_name, okPressed2 = QInputDialog.getText(self, "last name", "last name:", QLineEdit.Normal, "")

        if okPressed1 and okPressed2 and first_name != '' and last_name != '':
            return first_name, last_name
        else:
            return None, None

    @pyqtSlot()
    def change_arrival(self):
        print(self.tableWidget.currentIndex())
    @pyqtSlot()
    def ok_arrival(self):
        first_name = self.tableWidget.currentIndex().siblingAtColumn(1).data()
        last_name = self.tableWidget.currentIndex().siblingAtColumn(2).data()
        student = self.algo.find_student(first_name,last_name)
        flag = "לא אישר הגעה"
        print(self.tableWidget.currentIndex().siblingAtColumn(0).data())
        print(self.tableWidget.currentIndex().siblingAtColumn(1).data())
        print(self.tableWidget.currentIndex().siblingAtColumn(2).data())
        print(self.tableWidget.currentIndex().siblingAtColumn(3).data())
        if self.radioButton2.isChecked():
            self.wind.close()
            flag = "אישר הגעה"
        elif self.radioButton1.isChecked():
            self.wind.close()
        self.wind.close()
        self.algo.main_system.EVENT[self.event_name].arrival_confirmation[
            int(self.tableWidget.currentIndex().siblingAtColumn(0).data()) - 1] = (student,flag)

    @pyqtSlot()
    def arrival_doubleClicked(self):
        self.wind  = QDialog()
        self.radioButton1 = QRadioButton()
        self.radioButton2 = QRadioButton()
        self.radioButton1.setGeometry(QRect(150, 90, 95, 20))
        self.radioButton2.setGeometry(QRect(150, 90, 95, 20))
        self.radioButton1.setText("לא מגיע")
        self.radioButton2.setText("מגיע")
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.ok_arrival)
        self.buttonBox.rejected.connect(self.cancle)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.radioButton1)
        self.layout.addWidget(self.radioButton2)
        self.layout.addWidget(self.buttonBox)
        self.wind.setLayout(self.layout)
        self.wind.show()

    @pyqtSlot()
    def ok_equipment_list(self):
        self.algo.main_system.EVENT[self.event_name].equipment_list = self.textLine.toPlainText()
        self.wind.close()

    @pyqtSlot()
    def back(self):
        self.close()

    @pyqtSlot()
    def delete_event(self):
        self.msg = QDialog()
        buttonBox = QDialogButtonBox()
        buttonBox.setOrientation(Qt.Horizontal)
        buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.delete)
        buttonBox.rejected.connect(self.close_dialog)
        label = QLabel()
        label.setText("האם אתה בטוח שאתה רוצה למחוק?")
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(buttonBox)
        self.msg.setLayout(layout)
        x = self.msg.exec_()

    @pyqtSlot()
    def delete(self):
        self.algo.main_system.EVENT.pop(self.event_name)
        self.msg.close()
        self.close()

    @pyqtSlot()
    def close_dialog(self):
        self.msg.close()
