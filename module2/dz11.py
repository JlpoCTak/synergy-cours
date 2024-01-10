import numpy as np
import pandas as pd


def zadacha1():
    data_set = pd.read_csv('Customers.csv', sep=';')
    print(data_set)


def zadacha2():
    data_set = pd.read_csv('Customers.csv', sep=';')
    clean_data_set = data_set.dropna()
    print(clean_data_set)


def zadacha3():
    data_set = pd.read_csv('Customers.csv', sep=';')
    clean_data_set = data_set.dropna()
    grouped_data_set = clean_data_set.groupby('Profession')['Income'].agg(['mean'])
    print(grouped_data_set)

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
