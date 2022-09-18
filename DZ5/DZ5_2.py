# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
os.system("cls")
import my_function as mf
from random import randint

def get_first_move():
    '''
    Функция определяет случайным образом чей ход и выводит его на экран
    '''
    first_move = randint(0,1)
    if first_move == 0:
        print("Первым ходете Вы!")
    else:
        print("Первым хожу я!")
    return first_move

def check(sweet, sweets, mv, first_move, game_move) -> int:
    '''
    Функция проверяет ход игры и выявляет победителя.
    '''
    if sweet < sweets:
        sweets = sweets - sweet
        mv+=1
        return mv, sweets
    elif sweet >= sweets:
        sweets=0
        if game_move == 0:
            print(f"В этой игре Вы проиграли!")
        elif game_move == 1:
            print(f"В этой игре проиграл я!")
        exit(0)

def game(first_move, sweets, sweet_per_time):
    '''
    Функция получает на вход первого игрока и проводит процесс игры
    '''
    mv_0 = 0
    mv_1 = 0
    sweet = 1
    game_move = 0
    while sweets > 0:

        if first_move == 0:
           
            sweet = mf.get_number("Ваш ход: ", 1, sweet_per_time)
            game_move = 0
            mv_0, sweets = check(sweet, sweets, mv_0, first_move, game_move)
            print(f'Ваших ходов: {mv_0}, моих ходов: {mv_1}, осталось конфет {sweets}')
          
            if sweets < sweet_per_time:
                sweet = randint(1,sweets)
            else:
                sweet = randint(1,sweet_per_time)
            print(f"Мой ход: {sweet}")
            game_move = 1
            mv_1, sweets = check(sweet, sweets, mv_1, first_move, game_move)
            print(f'Ваших ходов: {mv_0}, моих ходов: {mv_1}, осталось конфет {sweets}')

        elif first_move == 1:

            if sweets < sweet_per_time:
                sweet = randint(1,sweets)
            else:
                sweet = randint(1,sweet_per_time)
            print(f"Мой ход: {sweet}")
            game_move = 1
            mv_1, sweets = check(sweet, sweets, mv_1, first_move, game_move)
            print(f'Ваших ходов: {mv_0}, моих ходов: {mv_1}, осталось конфет {sweets}')

            sweet = mf.get_number("Ваш ход: ", 1, sweet_per_time)
            game_move = 0
            mv_0, sweets = check(sweet, sweets, mv_0, first_move, game_move)
            print(f'Ваших ходов: {mv_0}, моих ходов: {mv_1}, осталось конфет {sweets}')
    
sweets = mf.get_number("Введите общее количество конфет: ")
sweets_per_time = mf.get_number("Введите максимальное (минимум = 1) количество конфет, которые можно взять за один раз, но не больше 1/3 от общего числа: ",0,int(sweets/3))
print("Определяем чей первый ход: ")
first_move = get_first_move()
game(first_move, sweets, sweets_per_time)

    
