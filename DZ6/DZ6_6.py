# Формат: Объясняет преподаватель

# **Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
import math
import my_function as mf
import os
os.system('cls')

num = mf.get_number("Введите количество членов последовательности: ",1)

array = [int(math.pow((-1), i)*3**i) for i in range(num)]

print(f'\nСписок из {num} членов последовательности: {array}\n')
