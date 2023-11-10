def chetnost():
    num = float(input('введите число:'))
    if num%2==0:
        print('Данное число четное')
    else:
        print('Данное число не является четным')

def bigger():
    num1 = int(input('Введите 1-е число:'))
    num2 = int(input('Введите 2-е число:'))
    print(max(num1, num2))

def chess():
    cletka1 = int(input())
    cletka2 = int(input())
    if (cletka1+cletka2) % 2 == 0:
        print('NO')
    else:
        print('YES')

def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)четность'
              '\n2)вывести большее'
              '\n3)проверка клетки'
              '\n4)выйти')
        a = int(input())
        if a == 1:
            chetnost()
        elif a == 2:
            bigger()
        elif a == 3:
            chess()
        else:
            break


main()
