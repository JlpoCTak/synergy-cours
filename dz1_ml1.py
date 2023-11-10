def rounded():
    num1 = float(input('введите число:'))
    num2 = int(input('введити до скольки знаков округлить:'))
    rez = round(num1, num2)
    print(rez)


def sred_arif():
    num1 = int(input('Введите 1-е число:'))
    num2 = int(input('Введите 2-е число:'))
    rez = round((num1+num2)/2)
    print(rez)


def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)окуглить число'
              '\n2)найти среднее арифметическое'
              '\n3)выйти')
        a = int(input())
        if a == 1:
            rounded()
        elif a == 2:
            sred_arif()
        else:
            break


main()
