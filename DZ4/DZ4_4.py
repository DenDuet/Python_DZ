# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ,
# считывает текст и дешифровывает его.


import my_function as mf
import os.path
import os
os.system("cls")


def make_file(file_name, string):
    '''
    Функция создает файл с данными и записывает его на диск, если его там не было.
    '''
    f = open(file_name, "w", encoding="UTF-8")
    f.write(string)
    f.close()


def read_file(file_name):
    '''
    Функция читает из файла строку текста.
    '''
    f = open(file_name, "r", encoding="UTF-8")
    string = f.readline()
    # string = string.encode('utf8')
    f.close()
    return string


def coding_liter(liter, number):
    '''
    Функция получает на вход букву и число, а возвращает букву со сдвигом на это число (регистр сохраняется). 
    Если число <0, то сдвиг влево и наоборот.
    '''
    min_str = 'a'
    max_str = 'z'
    min_prop = 'A'
    max_prop = 'Z'

    if ord(min_str) <= ord(liter) <= ord(max_str):
        # 26 количество букв латинского алфавита
        return chr(ord(min_str) + (ord(liter) - ord(min_str) + number) % 26)

    elif ord(min_prop) <= ord(liter) <= ord(max_prop):
        # 26 количество букв латинского алфавита
        return chr(ord(min_prop) + (ord(liter) - ord(min_prop) + number) % 26)

    else:
        return chr(ord(liter) + number)


def decoding_liter(liter, number):
    '''
    Функция получает на вход букву и число, а возвращает букву со сдвигом на это число (регистр сохраняется). 
    Если число <0, то сдвиг влево и наоборот.
     '''
    min_str = 'a'
    max_str = 'z'
    min_prop = 'A'
    max_prop = 'Z'

    if ord(min_str) <= ord(liter) <= ord(max_str):
        # 26 количество букв латинского алфавита
        return chr(ord(min_str) + (ord(liter) - ord(min_str) - number) % 26)

    elif ord(min_prop) <= ord(liter) <= ord(max_prop):
        # 26 количество букв латинского алфавита
        return chr(ord(min_prop) + (ord(liter) - ord(min_prop) - number) % 26)

    else:
        return chr(ord(liter) - number)


# abcdefghijklmnopqrstuvwxyz
def coding_text():
    '''
    Функция получает строку и кодирует её
    '''
    text = input("Введит строку: ")
    coding_txt = ''
    number = mf.get_number("Введите число, на которое сдвигать: ")
    for i in text:
        coding_txt = coding_txt + str(coding_liter(i, number))
    return number, text, coding_txt


def decoding_text(text, number):
    '''
    Функция получает строку и декодирует её
    '''
    decoding_txt = ''
    for i in text:
        decoding_txt = decoding_txt + str(decoding_liter(i, number))
    return decoding_txt


number, text, coding_txt = coding_text()
print(f"Оригинальная строка: {text} \nЗакодированная строка: {coding_txt}")
make_file("coding.txt", coding_txt)

f_coding_txt = read_file("coding.txt")
num = mf.get_number("\nВведите число сдвига: ")
decoding_txxt = decoding_text(f_coding_txt, num)

print(f"\nОригинальная строка из файла: {f_coding_txt} \nРаскодированная строка из файла: {decoding_txxt}")
