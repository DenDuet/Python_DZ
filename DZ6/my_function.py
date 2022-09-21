# _________________________________________________________________
# Файл с моими функциями, которые отсюда добавляются в мои проекты
# _________________________________________________________________

from random import randint


# _________________________________________________________________

def get_number(input_string, start=None, stop=None) -> int:
    '''
    Функция получает с клавиатуры целое число с проверкой корректности ввода.
    Можно передать число start и stop и, тогда будет ввод больше или равно start и меньше или равно stop
    '''
    while True:
        try:
            num = int(input(input_string))
            while (start != None and num < start) or (stop != None and num > stop):
                if num < start or num > stop:
                    num = int(input(input_string))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод!")

# _________________________________________________________________


def simple_numbers(number) -> bool:
    '''
    Функция получает число и проверяет его на предмет является оно простым или нет. Выдает ответ True или False
    '''
    k = 0
    for i in range(2, (number // 2)+1):
        if (number % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False

# _________________________________________________________________


def demult_numbers(number) -> list:
    '''
    Функция получает число и в списке выводит простые множители этого числа
    '''
    list_of_numbers = []
    for i in range(2, number+1):
        if number % i == 0:
            # используется функция из подключенного файла, проверяющая число на простоту
            if simple_numbers(i) == True:
                list_of_numbers.append(i)
    return list_of_numbers

# _________________________________________________________________


def list_of_numbers(number=None, min_n=None, max_n=None) -> list:
    '''
    Функция запрашивает количество чисел в списке, минимальное и максимальное число, заполняет список случайными числами из введенного диапазона.
    Заполненный список возвращает
    '''
    numbers = []
    if number==None: number = get_number("Введите количество чисел: ", 1)
    if min_n==None: min_n = get_number("Введите минимальное число в списке: ")
    if max_n==None: max_n = get_number("Введите максимальное число в списке: ")
    for i in range(number):
        numbers.append(randint(min_n, max_n))
    return numbers

# _________________________________________________________________


def delete_repeat_numbers(numbers) -> list:
    '''
    Функция удаляет из списка повторяющиеся символы и возвращает новый список без повторов
    '''
    numbers_list = []
    for i in numbers:
        if i not in numbers_list:
            numbers_list.append(i)
    return numbers_list

# _________________________________________________________________

def make_file(file_name, string):
    '''
    Функция создает файл с данными и записывает его на диск, если его там не было.
    '''
    f = open(file_name, "w", encoding="UTF-8")
    f.write(string)
    f.close()

# _________________________________________________________________


def read_file(file_name):
    '''
    Функция читает из файла строку текста.
    '''
    f = open(file_name, "r", encoding="UTF-8")
    string = f.readline()
    # string = string.encode('utf8')
    f.close()
    return string
