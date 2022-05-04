from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QLabel, QDialogButtonBox, QVBoxLayout, QPushButton


class GUIEditStudent(QDialog):
    def __init__(self, algo, student):
        super().__init__()
        self.title = 'כרטיס סטודנט'
        self.algo = algo
        self.student = student
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(251, 296)
        self.formLayout = QFormLayout()

        self.label = QLabel()
        self.label.setText("שם פרטי")
        self.lineEdit = QLineEdit()
        self.lineEdit.setText(self.student.first_name)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lineEdit)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)


        self.label_2 = QLabel()
        self.label_2.setText("שם משפחה")

        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setText(self.student.last_name)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEdit_2)

        self.label_3 = QLabel()
        self.label_3.setText("תעודת זהות")

        self.lineEdit_3 = QLineEdit()
        self.lineEdit_3.setText(str(self.student._id))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lineEdit_3)

        self.label_4 = QLabel()
        self.label_4.setText("מספר טלפון")

        self.lineEdit_4 = QLineEdit()
        self.lineEdit_4.setText(self.student.phone_number)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEdit_4)

        self.label_5 = QLabel()
        self.label_5.setText("כיתה")

        self.lineEdit_5 = QLineEdit()
        self.lineEdit_5.setText(self.student.grade)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_5)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lineEdit_5)

        self.label_6 = QLabel()
        self.label_6.setText("מין")

        self.lineEdit_6 = QLineEdit()
        self.lineEdit_6.setText(self.student.gender)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_6)
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lineEdit_6)

        self.label_7 = QLabel()
        self.label_7.setText("גיל")

        self.lineEdit_7 = QLineEdit()
        self.lineEdit_7.setText(str(self.student.age))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_7)
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lineEdit_7)

        self.label_8 = QLabel()
        self.label_8.setText("חוגים")

        self.lineEdit_8 = QLineEdit()
        text = ""
        if self.student.classes:
            for c in self.student.classes:
                text+=str(c)
            self.lineEdit_8.setText(text)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_8)
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lineEdit_8)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        button = QPushButton('מחק חניך', self)
        button.setGeometry(20, 20, 50, 50)
        button.clicked.connect(self.delete_employee)

        self.formLayout.setWidget(8,QFormLayout.LabelRole,self.buttonBox)
        self.formLayout.setWidget(8, QFormLayout.FieldRole, button)
        self.setLayout(self.formLayout)
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.accepted.connect(self.cancle)

    @pyqtSlot()
    def ok(self):
        self.algo.main_system.students[self.student._id].first_name = self.lineEdit.text()
        self.algo.main_system.students[self.student._id].last_name = self.lineEdit_2.text()
        self.algo.main_system.students[self.student._id].phone_number = self.lineEdit_4.text()
        self.algo.main_system.students[self.student._id].grade = self.lineEdit_5.text()
        self.algo.main_system.students[self.student._id].gender = self.lineEdit_6.text()
        self.algo.main_system.students[self.student._id].age = self.lineEdit_7.text()
        self.algo.main_system.students[self.student._id].classes.append(self.lineEdit_8.text())
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
            if self.student in self.algo.main_system.EVENT[event].arrival_confirmation[0]:
                x = []
                self.algo.main_system.EVENT[event].remove_participants(self.student)
        self.algo.main_system.students.pop(self.student._id)
        self.msg.close()
        self.close()

    @pyqtSlot()
    def close_dialog(self):
        self.msg.close()