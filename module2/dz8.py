import numpy as np

def check7(x):
    if x > 7:
        return True

def zadacha1():
    arr = np.random.randint(1, 11, size=100)
    print(arr)
    print()
    check_arr = np.apply_along_axis(check7, axis=0, arr=arr)

    print(check_arr)


def zadacha2():
    pass


def zadacha3():
    pass


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
