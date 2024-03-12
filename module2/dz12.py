import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt


def func(x):
    return (2*np.cos(x))/(sqrt(1+np.tan(x)**2))


def zadacha1():
    xlist = np.linspace(-10, 10, 100)
    y = [func(x) for x in xlist]
    plt.figure(figsize=(10, 5))
    plt.plot(xlist, y, linewidth=2, color='g', dashes=[8, 4], label='Вот такая моя функция', alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Титульник')
    plt.grid()
    plt.legend()
    plt.show()


def zadacha2():
    x = np.random.normal(0, 1, 3000)
    y = np.random.normal(3, 4, 3000)
    print(x)
    color = np.random.rand(3000)
    sizes = 100 * np.random.rand(x.shape[0])
    plt.scatter(x, y, c=color, s=sizes, alpha=0.5, marker='<')
    plt.annotate("график", xy=(3, 10), xytext=(2.8, 10),)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def zadacha3():
    data = np.random.normal(16, 2, 1000)
    plt.hist(data, bins=20, color='r', alpha=0.5)
    plt.show()
    #вывод: Большинство результатов стремится к интервалу от 13 до 18 секунд.
    #Столбики гистограммы снижаются с обеих сторон максимума, что указывает
    # на уменьшение количества результатов с увеличением времени забега.


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
