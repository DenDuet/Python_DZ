# Формат: Объясняет преподаватель

# **Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**
# 1- Определить, присутствует ли в заданном списке строк, некоторое число

import my_function as mf
from random import randint
import os
os.system('cls')

num = mf.get_number("Введите количество символов в массиве: ",1)
min_n = 0
max_n = 10
rand_num = randint(min_n,max_n)

list_numbers = [randint(min_n,max_n) for _ in range(num)]
new_list = list(filter(lambda x: x == rand_num, list_numbers))

print(f'\nВ списке: {list_numbers} число {rand_num} встречается {len(new_list)} раз(а)\n')