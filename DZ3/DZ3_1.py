# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

spisok = []

def get_number(input_string) -> int:
    '''
    функция получает с клавиатуры целое число (большее 0) с проверкой корректности ввода
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
        spisok.append(randint(0,11))
    
def list_sum(spisok) -> int:
    '''
    функция ищет элементы списка на нечетных позициях и их суммирует
    '''
    summa = 0
    for i in spisok[1::2]:
        summa = summa + i
    return summa

list_gen()    

print(f"Сумма элементов списка {spisok}, стоящих на нечетных позиция равна: {list_sum(spisok)}")