# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_number(input_string) -> int:
    '''
    функция получает с клавиатуры целое с проверкой корректности ввода
    '''
    while True:
        try:
            num = int(input(input_string))      
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод!")
            
def dvoichnoe_digit(num) -> int:
    '''
    функция принимает целое число и переводит его в двоичное
    '''
    dva_digit = ''
    number=num
    count=0
    if num<0:
        znak = '-0b'
        num=num*(-1)
    else:
        znak = '0b'
    
    while num>0:
        if num%2 == 0:
            dva_digit=dva_digit+'0'
        elif num%2>0 or num//2==1:
            dva_digit=dva_digit+'1'
        num=num//2
        count+=1
        if count%4==0:
            dva_digit=dva_digit+' '
    print(count)
    if count%4 !=0:
        for i in range(4-count%4):
            dva_digit=dva_digit+'0'
            
    dva_digit=dva_digit[::-1]
    print(f"Двоичное число десятичного {number} = {znak+dva_digit}")

            
number = get_number("Введите целое число: ")
# print(number)
dvoichnoe_digit(number)