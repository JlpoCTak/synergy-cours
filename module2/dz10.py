import numpy as np
import pandas as pd


def zadacha1():
    data_set = pd.read_csv('Customers.csv', sep=';')
    print(data_set)


def zadacha2():
    data_set = pd.read_csv('Customers.csv', sep=';')
    data_age_zp = data_set[(data_set['Age'] > 30) & (data_set['Income'] < 30000)]
    print(data_age_zp)
    print()
    data_prof = data_set[(data_set['Profession'] == 'Lawyer') & (data_set['Work Experience'] > 5)]
    print(data_prof)

def main():
    while True:
        print('Введите номер дейстивия'
              '\n1)задача1'
              '\n2)задача2'
              '\n3+)выход')
        a = input()
        if a == '1':
            zadacha1()
        elif a == '2':
            zadacha2()
        else:
            break


main()
