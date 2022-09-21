# Формат: Объясняет преподаватель

# **Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math
import my_function as mf
from random import randint
import os
os.system('cls')

numbers_str = input("Введите координаты точек (x, y) и (x1, y1) через пробел: ").split(" ")
numbers = list(map(float, numbers_str))
path = round(math.sqrt((numbers[2]-numbers[0])**2 + (numbers[3]-numbers[1])**2),2)
print(f"\nРасстояние между точками с координатами: ({numbers[0]}, {numbers[1]}) и ({numbers[2]}, {numbers[3]}) = {path}\n")