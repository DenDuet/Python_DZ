# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def get_coordinate():
    while True:
        try:
            num = int(input())
            while num == 0:
                print("Число должно быть больше или меньше 0!")
                num = int(input())
                continue
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод.")

            
def quarter(X,Y):
    if (X>0 and Y>0): print("Первая четверть [0 - ∞, 0 - ∞]")
    elif (X>0 and Y<0): print("Четвертая четверть [0 - ∞, -∞ - 0]")
    elif (X<0 and Y<0): print("Третья четверть [-∞ - 0, -∞ - 0]")
    elif (X<0 and Y>0): print("Вторая четверть [-∞ - 0, 0 - ∞]")

print("Введите число X отличное от 0: ")
X = get_coordinate()
print("Введите число Y отличное от 0: ")
Y = get_coordinate()

quarter(X,Y)