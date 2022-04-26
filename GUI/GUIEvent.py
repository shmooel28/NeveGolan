from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel


class GUIEvent(QDialog):
    def __init__(self, event):
        super().__init__()
        self.title = 'כרטיס אירוע'
        self.event = event
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(800, 800)
        self.formLayout = QFormLayout()

        self.label = QLabel()
        self.label.setText("שם אירוע")
        self.label_0 = QLabel()
        self.label_0.setText(self.event.event_name)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_0)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.label_2 = QLabel()
        self.label_2.setText("משתתפים")
        self.label_2_2 = QLabel()
        names = ''
        for p in self.event.arrival_confirmation:
            names += str(p[0])+'\n'
        self.label_2_2.setText(names)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2_2)

        '''self.label_3 = QLabel()
        self.label_3.setText("אנשי צוות")
        self.label_3_3 = QLabel()
        self.label_3_3.setText(self.event.employee)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3_3)'''

        self.label_4 = QLabel()
        self.label_4.setText("אישורי הגעה")
        self.label_4_4 = QLabel()
        self.label_4_4.setText(str(self.event.arrival_confirmation))
        # self.lineEdit_4 = QLineEdit()

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4_4)

        self.label_5 = QLabel()
        self.label_5.setText("רשימת ציוד")
        self.label_5_5 = QLabel()
        self.label_5_5.setText(self.event.equipment_list)
        # self.lineEdit_5 = QLineEdit()

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_5)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5_5)

        self.label_6 = QLabel()
        self.label_6.setText("תאריך")
        da = str(self.event.date.year) + '-' + str(self.event.date.month) + '-' + str(self.event.date.day)
        self.label_6_6 = QLabel()
        self.label_6_6.setText(da)
        # self.lineEdit_6 = QLineEdit()

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_6)
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6_6)

        self.label_7 = QLabel()
        self.label_7.setText("הערות")
        self.label_7_7 = QLabel()
        self.label_7_7.setText(self.event.comment)
        # self.lineEdit_7 = QLineEdit()

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_7)
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7_7)

        self.setLayout(self.formLayout)
