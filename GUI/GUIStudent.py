from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QLabel


class GUIStudent(QDialog):
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
        self.label_0 = QLabel()
        self.label_0.setText(self.student.first_name)
        #self.lineEdit = QLineEdit()


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_0)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)


        self.label_2 = QLabel()
        self.label_2.setText("שם משפחה")
        self.label_2_2 = QLabel()
        self.label_2_2.setText(self.student.last_name)
        #self.lineEdit_2 = QLineEdit()

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2_2)

        self.label_3 = QLabel()
        self.label_3.setText("תעודת זהות")
        self.label_3_3 = QLabel()
        self.label_3_3.setText(str(self.student._id))
        #self.lineEdit_3 = QLineEdit()

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3_3)

        self.label_4 = QLabel()
        self.label_4.setText("מספר טלפון")
        self.label_4_4 = QLabel()
        self.label_4_4.setText(self.student.phone_number)
        #self.lineEdit_4 = QLineEdit()

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4_4)

        self.label_5 = QLabel()
        self.label_5.setText("כיתה")
        self.label_5_5 = QLabel()
        self.label_5_5.setText(self.student.grade)
        #self.lineEdit_5 = QLineEdit()

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_5)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5_5)

        self.label_6 = QLabel()
        self.label_6.setText("מין")
        self.label_6_6 = QLabel()
        self.label_6_6.setText(self.student.gender)
        #self.lineEdit_6 = QLineEdit()

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_6)
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6_6)

        self.label_7 = QLabel()
        self.label_7.setText("גיל")
        self.label_7_7 = QLabel()
        self.label_7_7.setText(str(self.student.age))
        #self.lineEdit_7 = QLineEdit()

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_7)
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7_7)

        self.label_8 = QLabel()
        self.label_8.setText("חוגים")
        self.label_8_8 = QLabel()
        text = ""
        if not self.student.classes:
            text = "ללא חוגים עדיין"
        else:
            for c in self.student.classes:
                text += str(c)
            print(text)
        self.label_8_8.setText(text)
        # self.lineEdit_7 = QLineEdit()

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_8)
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8_8)
        self.setLayout(self.formLayout)