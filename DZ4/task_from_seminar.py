# 3. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Число N вводится пользователем.
# Позиции хранятся в файле file.txt в одной строке одно число
# Позиции в файл вам нужно программно положить в файл в зависимости от выбранного N: если пользователь введет двойку, то в файле вряд ли будут индексы 5 или 16.
# В решении должны быть и запись в файл, и чтение из файла.

from random import randint
import my_function as mf
import os.path
import os
os.system("cls")


def random_array() -> list:
    '''
    Функция формирует массив из запрошенного количества элементов от -N до N и заполняет его случайными числами
    '''
    number = mf.get_number("Введите количество элементов массива: ")
    numbers = []
    for i in range(number):
        numbers.append(randint(-number, number))
    return numbers


def make_index_array(array) -> list:
    '''
    Функция создает из массива array массив случайных индексов этого массива, количеством N/4
    '''
    index_numbers = ''
    number = mf.get_number("Введите количество множителей: ")
    for i in range(number):
        index_numbers = index_numbers + str(randint(0, len(array)-1)) + '\n'
    return index_numbers


def mult_numbers(array, index_for_mult) -> list:
    '''
    Функция получает на вход созданный массив чисел и массив индексов из файла и перемножает значения массива array по заданным индексам
    '''
    mult = 1
    for i in range(len(index_for_mult)):
        mult = mult*array[index_for_mult[i]]
    return mult


def make_file(file_name, string):
    '''
    Функция создает файл с данными (array) и записывает его на диск, если его там не было.
    '''
    f = open(file_name, "w", encoding="UTF-8")
    f.write(string)
    f.close()


def read_file(file_name):
    '''
    Функция читает из файла строку текста.
    '''
    with open(file_name) as file:
        index_for_mult = []
        for i in file:
            index_for_mult.append(int(i))
    return index_for_mult


array = random_array()
index_numbers = make_index_array(array)

make_file('index.txt', index_numbers)

if os.path.exists('index.txt') != False:
    index_for_mult = read_file("index.txt")
else:
    print("Нет файла индексов!")

mult = mult_numbers(array, index_for_mult)
print(f"У массива {array} случайным образом выбраны индексы {index_for_mult}. Произведение чисел массива по этим индексам = {mult}")
