# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8

import os
os.system("cls")
import my_function as mf

def make_taple(lang,num) -> list:
    '''
    Функция получает на вход 2 списка и делает из них кортеж 
    '''
    lang = [name.upper() for name in lang]
    taple = list(zip(num,lang))
    
    return taple
    
def filter_num(taple) -> list:
    '''
    Функция получает на вход кортеж и его фильтрует
    '''
    new_taple = []
    j1=0
    for i in range(len(taple)):
        word = taple[i][1]
        sum=0
        for j in range(len(word)):
            sum = sum + ord(word[j])
        numbers = mf.demult_numbers(sum)
        for k in numbers:
            if k == taple[i][0]:
                new_taple.append([])
                new_taple[j1].append(taple[i][0])
                new_taple[j1].append(taple[i][1])
                j1+=1
    return new_taple    
    

lang = ['python','c#','c++','java','assembler']
num = [1,2,3,4,5]

taple = make_taple(lang,num)
print(f'\nИз списков: {lang} и {num} -> \nсоздали список кортежей: {taple}')

taple_filtr = filter_num(taple)
print(f'\nУ элементов списка по заданному параметру остались такие варианты: {taple_filtr}\n')
