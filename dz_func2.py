from functools import reduce
def zadacha1():
    list1 = input('list1: ').split()
    list2 = input('list2: ').split()
    list3 = list(map(lambda x, y: int(x)+int(y), list1, list2))
    print(list3)


def zadacha2():
    def krat(num):
        if num//19 != 0 or num // 13 != 0:
            return True
        else:
            return False
    list1 = input('list: ').split()
    list1 = map(int, list1)
    list2 = list(filter(krat, list1))
    print(list2)


def zadacha3():
    list1 = input().split()
    print(reduce(max, list1))


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
