def zadacha1():
    n = int(input('введите кол-во городов '))
    city_list = []
    for i in range(n):
        city_list.append(input())
    k = 0
    for city in city_list:
        if city_list.count(city) > 1:
            k += 1
    print('вывод ', k)


def zadacha2():
    text = input('Введите текст ')
    text = text[0].upper()+text[1:].replace(f'{text[-1]}', f'{text[-1]}')
    for i in range(len(text)):
        if text[i-2] in '.?!':
            text = text[:i]+text[i].upper()+text[i+1:]
    text = text[:1]+text[1].lower()+text[2:]
    print(text)


def zadacha3():
    text1 = input().split()
    text2 = input().split()
    word_text1 = []
    word_text2 = []
    for i in range(len(text1)):
        word_text1.append(list(text1[i]))
    for i in range(len(text2)):
        word_text2.append(list(text2[i]))

    for i in range(1, len(word_text1)):
        for j in range(len(word_text1[i])):
            word_text1[0].append(word_text1[i][j])

    for i in range(1, len(word_text2)):
        for j in range(len(word_text2[i])):
            word_text2[0].append(word_text2[i][j])
    sym_text1 = set(word_text1[0])
    sym_text2 = set(word_text2[0])

    symm_dif = sym_text1 ^ sym_text2

    if list(symm_dif) == []:
        print('строки - анаграммы')
    else:
        print("строки - не анаграмы")


def zadacha4():
    text1 = input().split()
    text2 = input().split()
    text3 = input().split()
    c = set(text1) & set(text2) & set(text3)
    if list(c) != []:
        print(list(c).sort())
    else:
        print('Все три задачи никто не решил')



def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)задача1'
              '\n2)задача2'
              '\n3)задача3'
              '\n4)задача4'
              # '\n5)задача5'
              # '\n6)задача6'
              '\n5+)выход')
        a = int(input())
        if a == 1:
            zadacha1()
        elif a == 2:
            zadacha2()
        elif a == 3:
            zadacha3()
        elif a == 4:
            zadacha4()
        # elif a == 5:
        #     zadacha5()
        # elif a == 6:
        #     zadacha6()
        else:
            break


main()

