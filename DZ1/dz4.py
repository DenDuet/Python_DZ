# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def get_quarter():
    while True:
        try:
            num = int(input("Введите номер четверти (1-4): "))
            while ((num < 1) or (num>4)):
                print("Число должно быть от 1 до 4!")
                num = get_quarter()            
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
            
def quarter(num):
    if (num==1): print("Первая четверть [0 - ∞, 0 - ∞]")
    elif (num==4): print("Четвертая четверть [0 - ∞, -∞ - 0]")
    elif (num==3): print("Третья четверть [-∞ - 0, -∞ - 0]")
    elif (num==2): print("Вторая четверть [-∞ - 0, 0 - ∞]")

num = get_quarter()

quarter(num)