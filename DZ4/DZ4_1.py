# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import os
os.system("cls")

import my_function as mf


number = mf.get_number("Введите целое число: ")
print(f"У числа {number} простые множители: {mf.demult_numbers(number)}")
