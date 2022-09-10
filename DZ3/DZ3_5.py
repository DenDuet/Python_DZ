# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://clck.ru/yWbkX.)
#  F(-n)=(-1)^{n+1}

import math

fib_array = [0, 1]
fib_otr = []


def fib(number) -> list:
    '''
    функция возвращает список чисел Фибоначчи до заданного числа
    '''
    for i in range(2, number+1, 1):
        fib_array.append(fib_array[i-2]+fib_array[i-1])
    return fib_array


def fib_minus(number, fib) -> list:
    '''
    функция возвращает список чисел Фибоначчи до заданного отрицательного числа, получает его из списка положительных чисел
    '''
    fib_otr_array_new = []
    fib_otr_array_new = fib.copy()
    for i in range(1, number+1, 1):
        fib_otr_array_new[i] = int(math.pow((-1), i+1)*fib_otr_array_new[i])
    fib_otr_array_new.remove(0)
    fib_otr_array_new.reverse()
    return fib_otr_array_new


def result_fib(fib_otr, fib) -> list:
    '''
    функция возвращает список чисел Фибоначчи от заданного отрицательного до заданного положительного числа, объединением 2х списков
    '''

    for i in fib:
        fib_otr.append(i)
    return fib_otr


def get_number(input_string) -> int:
    '''
    функция получает с клавиатуры целое число с проверкой корректности ввода
    '''
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод!")


number = get_number("Введите целое число: ")
fib(number)

fib_otr = fib_minus(number, fib_array)

print(result_fib(fib_otr, fib_array))
