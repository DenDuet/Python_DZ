# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7;     
# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

import numbers
import my_function as mf
import os
os.system('cls')


number_list = []

def parse_string(number_str) -> list:
    '''
    Функция получает на вход строку с арифметическим выражением, а возвращает список значений и операндов
    '''
    i=0
    digit =''
    while i < len(number_str):
            if number_str[i].isdigit():
                digit=digit+number_str[i]
            elif digit=='':
                number_list.append(number_str[i])
            elif digit!='':
                number_list.append(int(digit))
                digit =''
                i-=1
            i+=1
    else:
        if digit!='':
                number_list.append(int(digit))
    if number_list[0] == '-':
        number_list[1] = number_list[1] *(-1)
        del number_list[0]
    return number_list
        
def check_list(number_list):
    '''
    Функция проверяет список на корректность, если не корректно, то выводит ошибку
    '''
    if number_list[-1] != ')' and not isinstance(number_list[-1], numbers.Number):
        print("Выражение содержит ошибку в конце строки. Исправьте!", number_list[-1])
        return False
    count1= [i for i in number_list if i=='(']          
    count2= [i for i in number_list if i==')']          
    if len(count1)!=len(count2):
        print("Выражение содержит ошибку. Непарные скобки. Исправьте!", number_list[-1])
        return False
        
    return True

def calc_numbers_3(first, sign, second) -> float:
    '''
    Функция получает список значений без скобок и выводит решение
    '''
    result=0
    if sign == '+':
        result = first + second
    elif sign == '-':
        result = first - second
    elif sign == '*':
        result = first * second
    elif sign == '/':
        if second!=0:
            result = first / second
        else:
            print("Получается деление на 0.")
            exit()
    return result
    
def calc_numbers(list_digit_sign) -> float:
    '''
    Функция получает список значений без скобок и выводит решение
    '''
    result=0
    if (len(list_digit_sign))==3:
            result=calc_numbers_3(list_digit_sign[0],list_digit_sign[1],list_digit_sign[2])
    elif (len(list_digit_sign))==5:
            if (list_digit_sign[1] == '+' or list_digit_sign[1] == '-') and (list_digit_sign[3] == '*' or list_digit_sign[3] =='/'):
                result = calc_numbers_3(list_digit_sign[2],list_digit_sign[3],list_digit_sign[4])
                result = calc_numbers_3(list_digit_sign[0],list_digit_sign[1], result)
            else: 
                result = calc_numbers_3(list_digit_sign[0],list_digit_sign[1],list_digit_sign[2])
                result = calc_numbers_3(result,list_digit_sign[3],list_digit_sign[4])
    return result
        
def calc_str(number_list) -> float:
    '''
    Функция получает на вход список значений и операндов и выводит решение
    '''
    if number_list==[]:
        return prom_rez
    i=0
    list_otkr_skobki = {}
    list_zakr_skobki = {}
    list_digit_sign = []
    skobki = 0
    for i in range(len(number_list)):
        if number_list[i] == '(':
            list_otkr_skobki[skobki] = i
            skobki +=1
        elif number_list[i] == ')':
            skobki-=1
            list_zakr_skobki[skobki] = i

    while len(list_otkr_skobki)>0:
        j = len(list_otkr_skobki)-1
        for i in range(list_otkr_skobki[j]+1,list_zakr_skobki[j]):
                list_digit_sign.append(number_list[i])
        prom_rez = calc_numbers(list_digit_sign)
        list_otkr_skobki[j]-=1
        list_zakr_skobki[j]+=1
        list_digit_sign=[]
        if list_otkr_skobki[j]+1 >=2 and isinstance(number_list[list_otkr_skobki[j]-1], numbers.Number) and (number_list[list_otkr_skobki[j]]=='*' or number_list[list_otkr_skobki[j]]=='/'):
            list_digit_sign.append(number_list[list_otkr_skobki[j]-1])
            list_digit_sign.append(number_list[list_otkr_skobki[j]])
            list_digit_sign.append(prom_rez)
            prom_rez = calc_numbers(list_digit_sign)
            list_otkr_skobki[j] = list_otkr_skobki[j] - 2

        if list_zakr_skobki[j] +1 <len(number_list) and isinstance(number_list[list_zakr_skobki[j]+1], numbers.Number) and (number_list[list_zakr_skobki[j]]=='*' or number_list[list_zakr_skobki[j]]=='/'):
            list_digit_sign=[]
            list_digit_sign.append(prom_rez)
            list_digit_sign.append(number_list[list_zakr_skobki[j]])
            list_digit_sign.append(number_list[list_zakr_skobki[j]+1])
            prom_rez = calc_numbers(list_digit_sign)
            list_zakr_skobki[j] = list_zakr_skobki[j] + 2

            if number_list[list_otkr_skobki[j]] == '(' and number_list[list_zakr_skobki[j]]==')':
                list_otkr_skobki[j]-=1
                list_zakr_skobki[j]+=1
        new_number_list = []
        skobki=0
        for k in range(len(number_list)): # перебираем заново массив с выражением
            if k>list_otkr_skobki[j] and k<list_zakr_skobki[j]:
                if k==list_otkr_skobki[j]+1: # чтобы только одно число добавилось
                    new_number_list.append(prom_rez)
            else:
                if number_list[k]=='(' or number_list[k] == ')':
                    skobki=1
                new_number_list.append(number_list[k]) 
        if new_number_list!=[]:
            if skobki==0:
                if len(new_number_list)>2: 
                    prom_rez = calc_numbers(new_number_list)
                number_list=[]
                return prom_rez
            elif skobki==1:
                if len(new_number_list)>2: 
                    prom_rez= calc_str(new_number_list)
                number_list=[]
                return prom_rez
    else: # если нету скобок вообще
        while number_list!=[]:
            list_sign = []
            sign=0
            for i in range(len(number_list)):
                if number_list[i] == '+' or number_list[i] == '-':
                    list_sign.append([])
                    list_sign[sign].append(i)
                    list_sign[sign].append(1) # приоритет второй важности
                    list_sign[sign].append(number_list[i]) 
                    sign+=1
                elif number_list[i] == '*' or number_list[i] == '/':
                    list_sign.append([])
                    list_sign[sign].append(i)
                    list_sign[sign].append(0) # приоритет первой важности
                    list_sign[sign].append(number_list[i]) 
                    sign+=1
            new_number_list = []
            prev_index=0
            costil=0
            for index, prior, sign in list_sign:
                if prior == 0:
                    if sign == '*':
                        number_list[index] = number_list[index+1] = number_list[index-1] = (float(number_list[index-1])*float(number_list[index+1])) 
                        if costil==0:
                            costil=index-1
                        if index == prev_index+2:
                            number_list[costil] = number_list[index+1]
                        prev_index=index
                    elif sign == '/':
                        if float(number_list[index+1])!=0:
                            number_list[index] = number_list[index+1] = number_list[index-1] = (float(number_list[index-1])/float(number_list[index+1]))
                            if costil==0:
                                costil=index-1
                            if index == prev_index+2:
                                number_list[costil] = number_list[index+1]
                            prev_index=index
                        else:
                            print("Получается деление на 0.")
                            exit()
                else: 
                    costil=0
            result=float(number_list[0])
            for index, prior, sign in list_sign:
                if prior == 1:
                    if sign == '+':
                        result = result + float(number_list[index+1])
                
                    elif sign == '-':
                        result = result - float(number_list[index+1])
            number_list = []
        return result
    
# number_str = '10 * 5 *'
# number_str = '((7*5)-(2+5*6)/6+10)+6'
# number_str = '(2+((5-3)*(16-14)))/3'
# number_str = '5+(7-14)'
number_str = '-2*(5+(2/(5-3)*(16-14)-4))/3'
# number_str = '-10+(110/(-7*3)-2)*2'
# number_str = '10+110/20+7*3-2*2' 
# number_str = '-10-25+40/20*4/2+7*3-2*2' 
#number_str = '((21+25*62)+10)+5+6'
    
print(f"Парсим строку: {number_str}")

number_list = parse_string(number_str)
print('\n', number_list)

if check_list(number_list):
    itog=calc_str(number_list)
    print(f"\nВыражение равно: {itog}\n")
