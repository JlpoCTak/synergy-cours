def zadacha1():
    num = input('введите число:')
    sum_num = 0
    for i in range(len(num)):
        sum_num += int(num[i])
    print(sum_num)


def zadacha2():
    n = int(input('введите n\n'))
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
def zadacha3():
    n = int(input('введите n\n'))
    for i in range(1, n+1):
        if i % 7 == 0:
            print(i)

def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)задача1'
              '\n2)задача2'
              '\n3)задача3'
              '\n4+)выход')
        a = int(input())
        if a == 1:
            zadacha1()
        elif a == 2:
            zadacha2()
        elif a == 3:
            zadacha3()
        else:
            break


main()
