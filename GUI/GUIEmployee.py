from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel


class GUIEmployee(QDialog):
    def __init__(self, employee):
        super().__init__()
        self.title = 'כרטיס איש צוות'
        self.employee = employee
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(270, 230)
        self.formLayout = QFormLayout()

        self.label = QLabel()
        self.label.setText("שם פרטי")
        self.label_0 = QLabel()
        self.label_0.setText(self.employee.first_name)
        #self.lineEdit = QLineEdit()


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_0)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)


        self.label_2 = QLabel()
        self.label_2.setText("שם משפחה")
        self.label_2_2 = QLabel()
        self.label_2_2.setText(self.employee.last_name)
        #self.lineEdit_2 = QLineEdit()

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2_2)

        self.label_3 = QLabel()
        self.label_3.setText("תעודת זהות")
        self.label_3_3 = QLabel()
        self.label_3_3.setText(str(self.employee._id))
        #self.lineEdit_3 = QLineEdit()

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3_3)

        self.label_4 = QLabel()
        self.label_4.setText("מספר טלפון")
        self.label_4_4 = QLabel()
        self.label_4_4.setText(self.employee.phone_number)
        #self.lineEdit_4 = QLineEdit()

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4_4)

        self.label_5 = QLabel()
        self.label_5.setText("מקצוע")
        self.label_5_5 = QLabel()
        self.label_5_5.setText(self.employee.speciality)
        #self.lineEdit_5 = QLineEdit()

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_5)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5_5)

        self.label_6 = QLabel()
        self.label_6.setText("מין")
        self.label_6_6 = QLabel()
        self.label_6_6.setText(self.employee.gender)
        #self.lineEdit_6 = QLineEdit()

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_6)
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6_6)

        self.label_7 = QLabel()
        self.label_7.setText("ימי עבודה")
        self.label_7_7 = QLabel()
        self.label_7_7.setText(str(self.employee.days))
        #self.lineEdit_7 = QLineEdit()

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_7)
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7_7)


        self.setLayout(self.formLayout)

