def zadacha1():
    print(input('введите строку: ').split()[::-1])


def zadacha2():
    text = input('Введите текст ')
    for i in range(len(text)):
        if i % 2 == 0:
            print(f'{text[i]}', end='')
    print()


def zadacha3():
    nums = input('ввод ').split()
    nums2 = []
    for i in range(len(nums)-1):
        nums2.append(int(nums[i]) ** int(nums[-1]))
    print(nums2)


def zadacha4():
    text = input('введите текст ')
    sym = input('введите символ ')
    new_text = text.replace(f'{sym}', f'{sym}{sym}')
    print(f'готовый текст {new_text}')


def zadacha5():
    text = input('Введите строку ')
    print('x: ', text.count('x'), ', y: ', text.count('y'))


def zadacha6():
    text = input('Введите строку ')
    count_ = text.count('(')
    for i in range(count_):
        index_start = text.find('(')
        index_end = text.find(')')
        print(text[index_start+1:index_end])
        text = text.replace(f'{text[0:index_end+1]}', '')


def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)задача1'
              '\n2)задача2'
              '\n3)задача3'
              '\n4)задача4'
              '\n5)задача5'
              '\n6)задача6'
              '\n7+)выход')
        a = int(input())
        if a == 1:
            zadacha1()
        elif a == 2:
            zadacha2()
        elif a == 3:
            zadacha3()
        elif a == 4:
            zadacha4()
        elif a == 5:
            zadacha5()
        elif a == 6:
            zadacha6()
        else:
            break


main()

