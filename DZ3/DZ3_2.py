# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

spisok = []
spisok_proizv = []


def get_number(input_string) -> int:
    '''
    функция получает с клавиатуры целое (число большее 3) с проверкой корректности ввода
    '''
    while True:
        try:
            num = int(input(input_string))
            while num <=2:
                num = int(input(input_string))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод!")


def list_gen() -> list:
    '''
    функция генерирует список случайных чисел от 0 до заданного числа в диапазоне [0,10]
    '''
    number = get_number("Введите число элементов списка (>2): ")
    for i in range(number):
        spisok.append(randint(0, 11))


def list_proizv(spisok) -> list:
    '''
    функция найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
    В нечетном списке средний элемент умножается сам на себя.
    '''
    for i in range(int(len(spisok)/2)):
        spisok_proizv.append(spisok[i]*spisok[len(spisok)-1-i])
    if len(spisok) % 2 != 0:
        spisok_proizv.append(spisok[len(spisok)-1-int(len(spisok)/2)]**2)


list_gen()
list_proizv(spisok)
print(f"Из элементов списка {spisok} получился список попарного перемножения чисел: {spisok_proizv}")
