from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QPushButton, QMessageBox, QVBoxLayout
from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel

class GUIEditEmployee(QDialog):
    def __init__(self, employee,algo):
        super().__init__()
        self.title = 'כרטיס איש צוות'
        self.employee = employee
        self.algo = algo
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(251, 296)

        self.formLayout = QFormLayout()

        self.label = QLabel()
        self.label.setText("שם פרטי")
        self.lineEdit = QLineEdit()
        self.lineEdit.setText(self.employee.first_name)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lineEdit)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)


        self.label_2 = QLabel()
        self.label_2.setText("שם משפחה")

        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setText(self.employee.last_name)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEdit_2)

        self.label_3 = QLabel()
        self.label_3.setText("תעודת זהות")

        self.lineEdit_3 = QLineEdit()
        self.lineEdit_3.setText(str(self.employee._id))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lineEdit_3)

        self.label_4 = QLabel()
        self.label_4.setText("מספר טלפון")

        self.lineEdit_4 = QLineEdit()
        self.lineEdit_4.setText(self.employee.phone_number)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEdit_4)

        self.label_5 = QLabel()
        self.label_5.setText("מקצוע")

        self.lineEdit_5 = QLineEdit()
        self.lineEdit_5.setText(self.employee.speciality)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_5)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lineEdit_5)

        self.label_6 = QLabel()
        self.label_6.setText("מין")

        self.lineEdit_6 = QLineEdit()
        self.lineEdit_6.setText(self.employee.gender)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_6)
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lineEdit_6)

        self.label_7 = QLabel()
        self.label_7.setText("גיל")

        self.lineEdit_7 = QLineEdit()
        self.lineEdit_7.setText(str(self.employee.age))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_7)
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lineEdit_7)

        self.label_8 = QLabel()
        self.label_8.setText("ניסיון")

        self.lineEdit_8 = QLineEdit()
        self.lineEdit_8.setText(str(self.employee.experience))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_8)
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lineEdit_8)

        self.label_9 = QLabel()
        self.label_9.setText("ימי עבודה")

        self.lineEdit_9 = QLineEdit()
        self.lineEdit_9.setText(str(self.employee.days))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_9)
        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lineEdit_9)

        self.label_10 = QLabel()
        self.label_10.setText("משכורת")

        self.lineEdit_10 = QLineEdit()
        self.lineEdit_10.setText(str(self.employee.salary))

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.label_10)
        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lineEdit_10)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        button = QPushButton('מחק עובד', self)
        button.setGeometry(20, 20, 50, 50)
        button.clicked.connect(self.delete_employee)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, button)
        self.formLayout.setWidget(10,QFormLayout.LabelRole,self.buttonBox)

        self.setLayout(self.formLayout)
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.cancle)

    @pyqtSlot()
    def ok(self):
        self.algo.main_system.employees[self.employee._id].first_name = self.lineEdit.text()
        self.algo.main_system.employees[self.employee._id].last_name = self.lineEdit_2.text()
        #self.algo.main_system.employees[self.employee._id]._id = self.lineEdit_3.text()
        self.algo.main_system.employees[self.employee._id].phone_number = self.lineEdit_4.text()
        self.algo.main_system.employees[self.employee._id].speciality = self.lineEdit_5.text()
        self.algo.main_system.employees[self.employee._id].gender = self.lineEdit_6.text()
        self.algo.main_system.employees[self.employee._id].age = self.lineEdit_7.text()
        self.algo.main_system.employees[self.employee._id].experience = self.lineEdit_8.text()
        self.algo.main_system.employees[self.employee._id].days = self.lineEdit_9.text()
        self.algo.main_system.employees[self.employee._id].salary = self.lineEdit_10.text()
        self.close()


    @pyqtSlot()
    def cancle(self):
        self.close()

    @pyqtSlot()
    def delete_employee(self):
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
        for event in self.algo.main_system.EVENT:
            if self.employee in self.algo.main_system.EVENT[event].employee:

                self.algo.main_system.EVENT[event].remove_employee(self.employee)
        self.algo.main_system.employees.pop(self.employee._id)
        self.msg.close()
        self.close()

    @pyqtSlot()
    def close_dialog(self):
        self.msg.close()