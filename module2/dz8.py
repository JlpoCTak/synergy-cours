import numpy as np


def zadacha1():
    arr = np.random.randint(1, 11, size=100)
    print(arr)
    print()
    check_arr = np.mean(arr > 7) * 100

    print("Ответ: ", check_arr, '%')


def zadacha2():
    proverka = 0
    for i in range(1001):
        arr = np.random.randint(1, 11, size=100)
        check_arr = np.mean(arr > 7) * 100
        if check_arr == 20:
            proverka += 1
    print(f"Ответ: {proverka}/1000")


def zadacha3():
    arr = np.tile(np.arange(1, 11), (10, 1))
    print(arr)


def zadacha4():
    arr = np.tile(np.arange(1, 11), (10, 1))
    sum_arr_y = arr.sum(axis=0)
    print(sum_arr_y)


def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)задача1'
              '\n2)задача2'
              '\n3)задача3'
              '\n4)задача4'
              '\n5+)выход')
        a = input()
        if a == '1':
            zadacha1()
        elif a == '2':
            zadacha2()
        elif a == '3':
            zadacha3()
        elif a == '4':
            zadacha4()
        else:
            break


main()
