# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# *Пример:*

# -n=2 => 2*x² + 4*x + 5 = 0 (коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x² = 0 (коэф: [10,0,0])

import random
import my_function as mf
import os
os.system("cls")

'''
n- степень икса первого элемента полинома (многочлена)
при n=3 -> 5*x**3 +18*x**2 + 7*x +19 = 0 - коэффициенты = [5,18,7,19]

коэффициенты - это числа перед элементами полинома.
коэффициенты могут быть 0, кроме первого
'''
def make_polinom() -> list:
    '''
    Функция запрашивает степень полинома и создает случайным образом (от 0 до 100) коэффициенты, возвращает список коэффициентов
    '''
    num = mf.get_number("Введите степень полинома: ", 1)
    number= mf.list_of_numbers(num+1,0,3)
    polinom=''

    if number[0]==0 and number[1]!=0: 
        number[0],number[1]=number[1],number[0]
    for i in range(len(number)-1):
        if i!=len(number)-2 and number[i] !=0: polinom = polinom + (str(number[i]) + ' * x^' + str(len(number)-1-i) + ' + ')
        elif i==len(number)-2:
            if number[i]!=0 and number[i+1]!=0: 
                polinom = polinom + str(number[i]) + ' * x + ' + (str(number[i+1]) + ' = 0 ')
            elif number[i]==0 and number[i+1] !=0:
                polinom = polinom + str(number[i+1]) + ' = 0 '
            elif number[i]!=0 and number[i+1] == 0:
                polinom = polinom + str(number[i]) + ' * x = 0 '
            else: 
                polinom = polinom + ' = 0 '
                
    return polinom
    

polinom = make_polinom()
print(f'Полином:\n {polinom}\n')

mf.make_file('polinom.txt', polinom)


