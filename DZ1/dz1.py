# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def get_week_day():
    while True:
        try:
            num = int(input("Введите число дня недели (1-7): "))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")

week_day = get_week_day()
if (0 < week_day < 8):
    if (week_day == 6 or week_day == 7):
        print("Выходной день")
    else:
        print("Рабочий день")
else:
    print("Это не день недели")
