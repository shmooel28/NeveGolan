from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QInputDialog, QLineEdit


class GUIShowTempStudent(QWidget):
    def __init__(self,algo, students,count):
        self.algo = algo
        self.students = students
        self.count =count
        super().__init__()
        self.title = ' '
        self.left = 0
        self.top = 0
        self.width = 1280
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.count + 1)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("number"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("first name"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("last name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("phone number"))
        self.tableWidget.move(0, 0)
        count = 1
        for s in self.students.values():
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(count)))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(s.first_name))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(s.last_name))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(s.phone_number))
            count += 1
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)

        self.button = QPushButton()
        self.button.setText('ייצוא לקובץ אקסל')
        self.button.clicked.connect(self.out_to_exl)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    @pyqtSlot()
    def out_to_exl(self):
        file_name = './'
        file_name += self.get_save_name()
        file_name += '.xlsx'
        self.algo.write_to_xlsx(file_name,self.students)

    def get_save_name(self):
        text, okPressed = QInputDialog.getText(self, "שם קובץ", "הכנס שם קובץ:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text
        else:
            return None