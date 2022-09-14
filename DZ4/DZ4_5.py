# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

import my_function as mf
import os.path
import os
os.system("cls")

msg = "AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool"
def make_file(file_name, string):
    '''
    Функция создает файл с данными (string) и записывает его на диск, если его там не было.
    '''
    f = open(file_name, "w", encoding="UTF-8")
    f.write(string)
    f.close()
    
def read_file(file_name):
    '''
    Функция читает данные из файла, обрабатывает их
    '''
    f = open(file_name, "r", encoding="UTF-8")
    string_l=f.read()
    f.close()
    return string_l

def make_shot_string(readed_msg) -> str:
    '''
    Функция получает на вход строку и кодирует её с помощью RLE кодирования
    '''
    coded_string = ''
    liter=readed_msg[0]
    counter=1
                    
    for i in range(1,len(readed_msg)):
        if liter==readed_msg[i]:
            counter+=1
            if i==len(readed_msg)-1:
                coded_string = coded_string + str(counter) + str(liter)
                print("         ",liter, i, coded_string)
        else:
            coded_string = coded_string + str(counter) + str(liter)
            liter=readed_msg[i]
            counter=1
    else:
        coded_string = coded_string + str(counter) + str(liter)
    return coded_string

def decoding_string(coded_string) -> str:
    '''
    Функция получает на вход кодированную (RLE метод) строку и декодирует её
    '''
    num_s = ''
    decoded_string=''
    for i in range(len(coded_string)):
        if coded_string[i].isdigit():
            num_s=num_s+coded_string[i]
        else:
            for j in range(int(num_s)):
                decoded_string=decoded_string+coded_string[i]
            num_s=''
    return decoded_string        
        

if os.path.exists('msg_input.txt')!=True:
    print("Создаем файл")
    make_file('msg_input.txt', msg)
    
readed_msg=read_file('msg_input.txt')
print(f"Сообщение, прочитанное из файла (длина {len(readed_msg)} символов):\n      {readed_msg}")

coded_string=make_shot_string(readed_msg)
make_file('msg_output.txt', coded_string)
print(f"Сообщение, закодированное и сохраненное в файл (длина {len(coded_string)} символов):\n      {coded_string}")

readed_msg=read_file('msg_output.txt')
decoded_string=decoding_string(readed_msg)
print(f"Кодированное сообщение, прочитанное из файла и раскодированное (длина {len(decoded_string)} символов):\n      {decoded_string}")
