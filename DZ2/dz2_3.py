# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

from pickle import FALSE, TRUE

def get_number(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод!")
            
def invert_str(string_input):
    return ''.join(reversed(string_input))

def if_palindrom(string_original, string_inverted):
    if string_original == string_inverted:
        print(f"Это число {string_original} является палиндромом")   
        return TRUE
    else:
        print(f"Это число {string_original} не является палиндромом")   
        return FALSE
            
number = get_number("Введите целое число: ")

str_number = str(number)
str_number_invert = invert_str(str_number)
count=0

while if_palindrom(str_number, str_number_invert)!=TRUE:
    str_number = str(int(str_number) + int(str_number_invert))
    str_number_invert = invert_str(str_number)
    count+=1
    print(f"Шаг итерации = {count}")
     