# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 
# 'абвгдейка - это передача' = >" - это передача"

import os
os.system("cls")

def input_string(input_msg, test_str) -> str:
    '''
    Функция запрашивает строку и возвращает её, либо, если строка пустая, то тестовую строку
    ''' 
    stroka = input(input_msg)
    if stroka == '':
        stroka = test_str
    return stroka
    
def cut_string(input_msg, cut_msg) -> str:
    '''
    Функция получает на вход искомую строку, делит её на отдельные слова, по символу пробела, в них ищет строку cut_msg и все слова, которые
    не содержат этой подстроки, складываются в новую строку, которая возвращается
    '''
    out_string = ''
    input_msg = input_msg.split()
    for str in input_msg:
        if not cut_msg in str:
            out_string = out_string + ' ' + str
    return out_string
    
stroka = input_string("Введите строку: ",'абвгдейка - это передача')
sub_stroka = input_string("Введите подстроку: ",'абв')
out_string = cut_string(stroka, sub_stroka)
print(f'\nВ строке: "{stroka}" \nищем подстроку: "{sub_stroka}", \nи вырезаем слова её содержащие: "{out_string}"\n')