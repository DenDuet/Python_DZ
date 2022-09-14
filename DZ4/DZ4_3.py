# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

import os.path
import os
os.system("cls")

import my_function as mf

array = "Волков Андрей, 5 \nНаталья Тарасова, 5 \nФредди Меркури, 3 \nДенис Байцуров, 4 \n"

def make_file(file_name, string):
    '''
    Функция создает файл с данными (array) и записывает его на диск, если его там не было.
    '''
    f = open(file_name, "w", encoding="UTF-8")
    f.write(string)
    f.close()
    
def read_file(file_name):
    '''
    Функция читает данные из файла, обрабатывает их
    '''
    f = open(file_name, "r", encoding="UTF-8")
    string_l=''
    for line in f:
        string_list = line.strip().split(" ")
        if int(string_list[2]) > 4:
            string_list[0] = string_list[0].upper()
            string_list[1] = string_list[1].upper()
        print(string_list[0] + " " + string_list[1] + " " + string_list[2])  
        string_l = string_l + string_list[0] + " " + string_list[1] + " " + string_list[2] + " \n"
    f.close()
    return string_l
    
if os.path.exists('list.txt')!=True:
    print("Создаем файл")
    make_file('list.txt', array)

string_list=read_file('list.txt')
make_file('return_list.txt', string_list)