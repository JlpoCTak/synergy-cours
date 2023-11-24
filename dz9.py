from functools import reduce
def zadacha1():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    def num3(num1, num2):
        num3.mul = num3.mul + num2
        if ((num3.mul % num1 == 0) and (num3.mul % num2 == 0)):
            return num3.mul
        else:
            num3(num1, num2)
        return num3.mul

    num3.mul = 0

    if (num1 > num2):
        m1 = num3(num2, num1)
    else:
        m1 = num3(num1, num2)
    print("наименьшее общее кратное:")
    print(m1)


def zadacha2():
    lst = []
    n = int(input('n = '))
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)


def zadacha3():
    lst = []
    n = int(input('n = '))
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    print(lst)


def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)задача1'
              '\n2)задача2'
              '\n3)задача3'
              '\n4+)выход')
        a = input()
        if a == '1':
            zadacha1()
        elif a == '2':
            zadacha2()
        elif a == '3':
            zadacha3()
        else:
            break


main()
