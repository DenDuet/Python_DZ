# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.01] => 0.19 или 19
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import random

spisok = []

def get_number(input_string) -> int:
    '''
    функция получает с клавиатуры целое (число большее 0) с проверкой корректности ввода
    '''
    while True:
        try:
            num = int(input(input_string))
            while num <=0:
                num = int(input(input_string))            
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод!")


def list_gen() -> list:
    '''
    функция генерирует список случайных чисел от 0 до заданного числа в диапазоне [0,10]
    '''
    number = get_number("Введите число элементов списка: ")
    for i in range(number):
        spisok.append(round(random.uniform(0.01, 9.99),2))
        
def list_transform(spisok) -> int:
    '''
    функция ищет в заданном массиве максимальное и минимальное значение дробной части и считает их разницу
    '''
    spisok_prom = []
    for i in spisok:
        spisok_prom.append(round((i-int(i))*100))
    # print(spisok_prom)   
    return max(spisok_prom), min(spisok_prom) 


list_gen()

max, min = list_transform(spisok)

print(f"В массиве {spisok} разница между максимальным {max} и минимальным {min} значением дробной части равна {max-min}")
