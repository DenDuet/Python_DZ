# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import struct
import time


def invert_str(string_input):
    return ''.join(reversed(string_input))


def random(min, max):
    rand_int = time.perf_counter_ns()
    str_rand_int = invert_str(str(rand_int/10))
    rand_int_new = float(str_rand_int)**2*100
    rand = min+int(rand_int_new*(max-min))
    return rand


def get_number(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод!")


min = get_number("Введите минимальное число: ")
max = get_number("Введите максимальное число: ")

massiv = []
for i in range(10):
    massiv.append(random(min, max+1))
print(f"Список из 10 случайных элементов от [{min} до {max}] - {massiv}")
