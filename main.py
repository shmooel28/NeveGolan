import sys
from datetime import date
from doctest import Example

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()
if __name__ == '__main__':
    import os
    print("Work dir:" + os.getcwd())

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    '''first_try = Algo()
    temp_student = Student("shmuel","Ben_David",123456789,"male",16,7,"0545798744",["math","music"])
    first_try.main_system.add_student(temp_student)
    temp_emp = Employee("sara","choen",254654789,"female",25,"mange","025564234",2,7000)
    first_try.main_system.add_employee(temp_emp)
    first_try.main_system.remove_student(temp_student)
    first_try.load_from_json("data/first_try.json")
    first_try.save_to_json("data/first_try_save.json")'''
    #d = date(2022,3,16)
    #print(d.day)
    #porim = Event('porim',d)
    #print(porim.count_down().days)

    '''row = 17
    col = 5
    a='&'
    b='*'
    arr_1 = [[0 for _ in range(row)] for _ in range(col)]
    arr_2 = [[0 for _ in range(row)] for _ in range(col)]
    count_i = col-1
    count_j = row -1
    for i in range(col):
        for j in range(row):
            arr_1[i][j] = min(i,j)
            arr_2[count_i][count_j] = arr_1[i][j]
            count_j -=1
        count_i -= 1
        count_j = row -1

    for i in range(col):
        for j in range(row):
            if min(arr_1[i][j],arr_2[i][j])%2==0:
                print(a,end="")
            else:
                print(b,end="")
        print()'''
