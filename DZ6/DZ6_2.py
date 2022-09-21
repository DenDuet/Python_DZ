# Формат: Объясняет преподаватель

# **Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

# 2- Найти сумму чисел списка стоящих на нечетной позиции

from functools import reduce
import my_function as mf
from random import randint
import os
os.system('cls')

num = mf.get_number("Введите количество символов в массиве: ",1)

min_n = 0
max_n = 10

list_numbers = [randint(min_n,max_n) for _ in range(num)]
new_list = reduce(lambda x,y: x + y, list_numbers[1::2])

print(f'\nСумма элементов списка: {list_numbers}, стоящих на нечетных позициях = {new_list}\n')