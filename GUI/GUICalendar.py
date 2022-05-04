from datetime import date

from PyQt5.QtCore import pyqtSlot, Qt, QPoint, QRectF
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QCalendarWidget, QTextEdit, QPushButton, QHBoxLayout, QWidget, QFormLayout


class GUICalendar(QCalendarWidget):
    def __init__(self, algo):
        super().__init__()
        self.algo = algo
        self.textBox = QTextEdit(self)
        self.textBox.setGeometry(0, 0, 300, 350)
        self.textBox.move(500, 0)
        font = QFont()
        font.setPointSize(18)
        font.setFamily(u"Microsoft YaHei")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.textBox.setFont(font)

        self.save_button = QPushButton()
        self.save_button.setGeometry(0, 0, 300, 30)
        self.save_button.move(100, 350)
        self.save_button.setText("save")
        self.save_button.setStyleSheet(u"background-color:yellow;\ncolor:blue;\nborder-radius:10")
        self.layout = QFormLayout()
        self.setGeometry(0, 0, 500, 350)
        self.selectionChanged.connect(self.change_date)
        self.save_button.clicked.connect(self.save_task)
        self.layout.setWidget(0,QFormLayout.LabelRole,self)
        self.layout.setWidget(0,QFormLayout.FieldRole,self.textBox)
        self.layout.setWidget(1,QFormLayout.FieldRole,self.save_button)
        if self.selectedDate().toPyDate().strftime("%d-%m-%Y") in self.algo.main_system.task:
            self.textBox.setText(
                self.algo.main_system.task[self.selectedDate().toPyDate().strftime("%d-%m-%Y")])
        else:
            self.textBox.setText(" ")

        self.win = QWidget()
        self.win.setLayout(self.layout)
        self.win.resize(850,450)
        self.win.show()

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)
        if date.toPyDate().strftime("%d-%m-%Y") in self.algo.main_system.task:
            painter.setBrush(Qt.red)
            painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 3, 3)
    @pyqtSlot()
    def save_task(self):
        self.algo.main_system.task[
            self.selectedDate().toPyDate().strftime("%d-%m-%Y")] = self.textBox.toPlainText()
        temp_task = self.algo.main_system.task.copy()
        for task in temp_task:
            if self.algo.main_system.task[task] == "" or self.algo.main_system.task[task] == ' ':
                self.algo.main_system.task.pop(task)

    @pyqtSlot()
    def change_date(self):
        if self.selectedDate().toPyDate().strftime("%d-%m-%Y") in self.algo.main_system.task:
            self.textBox.setText(
                self.algo.main_system.task[self.selectedDate().toPyDate().strftime("%d-%m-%Y")])
        else:
            self.textBox.setText(" ")




