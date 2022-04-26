# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def check_int(num: str):
    num_len = len(num)
    index = 0
    for i in range(num_len):
        if num[index] < '0' or num[index] > '9':
            print("this isn't number! pleas enter ID")
            return False
        index += 1
    return True


def number_of_digit(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    if count == 9:
        return True
    print('wrong number of digit')
    return False


def check_number(num):
    if check_int(num):
        num = int(num)
    else:
        exit()
    if not number_of_digit(num):
        exit()
    sum, index = 0, 0
    for i in range(9):
        temp = (num % 10) * ((index % 2) + 1)
        if temp >= 10:
            temp = temp % 10 + temp // 10
        sum += temp
        index += 1
        num //= 10
    print(sum)
    if sum % 10 == 0:
        return True


def check_password(password: str):
    if len(password) < 8 or len(password) > 16:
        return False
    count_digit_lower = 0

    for l in password:
        if l.isdigit() or l.islower():
            count_digit_lower += 1
        elif l.isspace():
            return False
    if len(password) == count_digit_lower:
        return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hello!! pleas enter ID')
    id_number = input()
    if check_number(id_number):
        print("This is True ID!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
