# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def get_coordinate_X():
    while True:
        try:
            X = int(input("Введите число X: "))
            while X == 0:
                print("Y должен быть больше 0!")
                X = get_coordinate_X()            
            return X
        except ValueError:
            print("Вы ввели не число. Повторите ввод")

def get_coordinate_Y():
    while True:
        try:
            Y = int(input("Введите число Y: "))
            while Y == 0:
                print("Y должен быть больше 0!")
                Y = get_coordinate_Y()
            return Y
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
            
def quarter(X,Y):
    if (X>0 and Y>0): print("Первая четверть [0 - ∞, 0 - ∞]")
    elif (X>0 and Y<0): print("Четвертая четверть [0 - ∞, -∞ - 0]")
    elif (X<0 and Y<0): print("Третья четверть [-∞ - 0, -∞ - 0]")
    elif (X<0 and Y>0): print("Вторая четверть [-∞ - 0, 0 - ∞]")

X = get_coordinate_X()
Y = get_coordinate_Y()

quarter(X,Y)