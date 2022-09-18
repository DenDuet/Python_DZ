# 2 - Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.

import random
import my_function as mf
import os
os.system("cls")

def make_polinom(num=3,min=0,max=3) -> list:
    '''
    Функция запрашивает степень полинома и создает случайным образом (от 0 до 100) коэффициенты, возвращает список коэффициентов в списке
    '''
    a=1 # делаем бесконечный цикл
    while a==1:
        number= mf.list_of_numbers(num+1,min,max)
        if number[0]!=0:
            break
            
    numbers = []
    for i in range(len(number)):
        numbers.append([])
        numbers[i].append(number[i])
        numbers[i].append(len(number)-1-i)
    return numbers
        
def make_polinom_from_list(number) -> list:
    '''
    Функция получает список элементов и коэффициентов и делает полином
    '''
    polinom=''
    for i in range(len(number)):
        if number[i][0] != 0 and number[i][1]>1:
            if i !=0: 
                polinom = polinom + ' + '
            polinom = polinom + str(number[i][0]) + ' * x^' + str(number[i][1])
        elif number[i][0] != 0 and number[i][1]==1:
            if i !=0: 
                polinom = polinom + ' + '
            polinom = polinom + str(number[i][0]) + ' * x'

        elif number[i][0] != 0 and number[i][1] == 0:
            if i !=0: 
                polinom = polinom + ' + '
            polinom = polinom + str(number[i][0])
    else:        
        polinom = polinom + ' = 0'
    return polinom
    
def parse_polinom(polinom) -> list:
    '''
    Функция получает полином в виде строки и разбирает его на составные части
    '''
    numbers = []
        
    polinom = polinom.split(' + ')
    len_polinom = len(polinom)
    j=0
    for i in range(len_polinom):
        polinom[i] = polinom[i].split()
        try:
            polinom[i][2]=polinom[i][2].split('^')
        except:
            polinom[i][2]=polinom[i][2].split('=')
        
        if i==0:
            numbers_new = []
            for j in range(int(polinom[0][2][-1])+1):
                numbers_new.append([])
                numbers_new[j].append(0)
                numbers_new[j].append(int(polinom[0][2][-1])-j)   
                  
        if polinom[i][1] == '*':
            if polinom[i][2][-1] !='x':
                for k in range(len(numbers_new)):
                    if numbers_new[k][1] == int(polinom[i][2][-1]):
                        numbers_new[k][0]=int(polinom[i][0])
            else:
                for k in range(len(numbers_new)):
                    if numbers_new[k][1] == 1:
                        numbers_new[k][0]=int(polinom[i][0])
        elif polinom[i][1] == '=':
                for k in range(len(numbers_new)):
                    if numbers_new[k][1] == int(polinom[i][2][-1]):
                        numbers_new[k][0]=int(polinom[i][0])
    return numbers_new

def sum_polinom(polinom_f,polinom_s) -> list:
    '''
    Функция получает 2 полинома и возвращает их сумму в списке
    '''
    sum_polinom = []
    for i in range(len(polinom_f)):
        sum_polinom.append([])
        sum_polinom[i].append(polinom_f[i][0] + polinom_s[i][0])
        sum_polinom[i].append(polinom_f[i][1])
    return sum_polinom
        
number = mf.get_number("Введите степень полинома: ", 1)

numbers = make_polinom(number)
polinom_f = make_polinom_from_list(numbers)

print(f'Полином №1:\n {polinom_f}\n')
mf.make_file('polinom1.txt', polinom_f)

numbers = make_polinom(number)
polinom_s = make_polinom_from_list(numbers)
print(f'Полином №2:\n {polinom_s}\n')
mf.make_file('polinom2.txt', polinom_s)

readed_polinom_first = mf.read_file('polinom1.txt')
print(f'Полином, прочитанный из файла:\n {readed_polinom_first}\n')
numbers_first = parse_polinom(readed_polinom_first)

readed_polinom_second = mf.read_file('polinom2.txt')
print(f'Полином, прочитанный из файла:\n {readed_polinom_second}\n')
numbers_second = parse_polinom(readed_polinom_second)

sum_polinom = sum_polinom(numbers_first,numbers_second)
sum_polinom_str = make_polinom_from_list(sum_polinom)
print(f'Полином суммарный:\n {sum_polinom_str}\n')
mf.make_file('polinom_sum.txt', sum_polinom_str)