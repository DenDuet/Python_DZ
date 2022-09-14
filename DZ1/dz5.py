# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def get_coordinate(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
            
x1 = get_coordinate("Введите координату x первой точки: ")
y1 = get_coordinate("Введите координату y первой точки: ")
x2 = get_coordinate("Введите координату x второй точки: ")
y2 = get_coordinate("Введите координату y второй точки: ")

print(f"Расстояние между точкой A({x1},{y1}) и B({x2},{y2}) равно {round(math.sqrt((x2-x1)**2 + (y2-y1)**2),2)}")
