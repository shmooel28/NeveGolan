from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QGridLayout, QCheckBox, QLineEdit, QLabel, QSpinBox, QDialogButtonBox, \
    QTableWidget, QTableWidgetItem, QMessageBox, QVBoxLayout, QPushButton

from GUIShowTempStudent import GUIShowTempStudent


class GUIFilterStudent(QDialog):
    def __init__(self,algo,event_name = None):
        super().__init__()
        self.event_name = None
        if event_name:
            self.event_name = event_name
        self.from_age = 0
        self.to_age = 100
        self.from_grade = 'א'
        self.to_grade = 'יב'
        self.gender = 'ז,נ'
        self.gender_flag = False
        self.resize(422, 308)
        self.title = "סינון"
        self.okey = False
        self.algo = algo
        self.temp_student_list = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.gridLayout = QGridLayout()
        self.checkBox_3 = QCheckBox()
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 2)
        self.checkBox_2 = QCheckBox()
        self.gridLayout.addWidget(self.checkBox_2, 0, 5, 1, 2)
        self.checkBox = QCheckBox()
        self.gridLayout.addWidget(self.checkBox, 0, 8, 1, 2)
        self.lineEdit_2 = QLineEdit()
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.label_4 = QLabel()
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.lineEdit = QLineEdit()
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.label_3 = QLabel()
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.spinBox_2 = QSpinBox()
        self.gridLayout.addWidget(self.spinBox_2, 1, 4, 1, 1)
        self.label_2 = QLabel()
        self.gridLayout.addWidget(self.label_2, 1, 5, 1, 1)
        self.spinBox = QSpinBox()
        self.gridLayout.addWidget(self.spinBox, 1, 6, 1, 1)
        self.label = QLabel()
        self.gridLayout.addWidget(self.label, 1, 7, 1, 1)
        self.checkBox_5 = QCheckBox()
        self.gridLayout.addWidget(self.checkBox_5, 1, 8, 1, 1)
        self.checkBox_4 = QCheckBox()
        self.gridLayout.addWidget(self.checkBox_4, 1, 9, 1, 1)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 5)
        self.checkBox_3.setText("כיתה")
        self.checkBox_2.setText("גיל")
        self.checkBox.setText("מין")
        self.label_4.setText("עד")
        self.label_3.setText("מ")
        self.label_2.setText("עד")
        self.label.setText("מ")
        self.checkBox_5.setText("נ")
        self.checkBox_4.setText("ז")
        self.setLayout(self.gridLayout)

        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.cancle)

    @pyqtSlot()
    def ok(self):
        if self.checkBox.isChecked():
            self.gender_flag = True
            if self.checkBox_5.isChecked():
                self.gender = 'נ'
            if self.checkBox_4.isChecked():
                self.gender = 'ז'
        if self.checkBox_2.isChecked():
            self.from_age = self.spinBox.text()
            self.to_age = self.spinBox_2.text()
        if self.checkBox_3.isChecked():
            self.from_grade = self.lineEdit.text()
            self.to_grade = self.lineEdit_2.text()
        count,self.temp_student_list = self.algo.filter_student(self.from_age,self.to_age,self.from_grade,self.to_grade,self.gender_flag,self.gender)
        if count == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('ERROR- cannot find any students')
            x = msg.exec_()
        else:
            if self.event_name:
                for student in self.temp_student_list.values():
                    self.algo.main_system.EVENT[self.event_name].add_participants(student)
            self.close()
            self.new_window = GUIShowTempStudent(self.algo,self.temp_student_list,count)
            self.new_window.show()
    @pyqtSlot()
    def cancle(self):
        self.close()

    def get_students(self):
        return self.temp_student_list
