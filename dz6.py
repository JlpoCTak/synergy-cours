def zadacha1(text) -> bool:
    flag = True
    for i in range(int((len(text)/2)//1)):
        if text[i] == text[::-1][i]:
            continue
        else:
            flag = False
            break
    return flag


def zadacha2(name, sec_name, fath_name, age) -> str:
    birth = 2023 - int(age)
    return f'{sec_name} {name} {fath_name} {birth} г.р. зарегистрирован'

def zadacha3(nums: list) -> int:
    max_num = nums[0]
    for i in range(len(nums)):
        if max_num <= nums[i]:
            max_num = nums[i]
    return max_num


def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)задача1'
              '\n2)задача2'
              '\n3)задача3'
              '\n4+)выход')
        a = int(input())
        if a == 1:
            text = input()
            print(zadacha1(text))
        elif a == 2:
            name = input('Имя: ')
            sec_name = input("Фамилия: ")
            fath_name = input("Отчество: ")
            age = input("Возраст: ")
            print(zadacha2(name, sec_name, fath_name, age))
        elif a == 3:
            nums = list(input(f'Введите 2-3 числа через пробел\n').split())
            for i in range(len(nums)):
                if nums[i] is None:
                    nums = nums.remove(nums[i])
                else:
                    nums[i] = int(nums[i])
            print(zadacha3(nums))

        else:
            break
            

main()
