# 1 - Создайте программу для игры в ""Крестики-нолики"".

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint


def new_game():
    
    global first_move
    global my_char
    global comp_char
    first_move = randint(0,1)
    if first_move == 0:
        text="Первым ходите Вы! \nВаши - 'O'"
        my_char='O'
        comp_char = 'X'
    else:
        text="Первым хожу я! \nМои - 'O'"
        my_char='X'
        comp_char = 'O'
    messagebox.showinfo("Ход",text)
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lightblue'
    if comp_char=='O':
        comp_move()
        
    # fm.mainloop()    
    
def end_game(whose_char):
    '''
    Функция выводит окно с выигравшим
    '''
    if whose_char==my_char:
        text = 'Вы победили!'
    else:
        text = 'Я победил!'
    messagebox.showinfo('Победитель',text)

def check_res(whose_char):
    '''
    Функция проверяет комбинацию на выигрыш
    '''
    for r in range(3):
        if field[r][0]['text'] == field[r][1]['text'] == field[r][2]['text'] == whose_char:
            return 'win'
        if field[0][r]['text'] == field[1][r]['text'] == field[2][r]['text'] == whose_char:
            return 'win'
    if field[0][0]['text'] == field[1][1]['text'] == field[2][2]['text'] == whose_char:
        return 'win'
    if field[0][2]['text'] == field[1][1]['text'] == field[2][0]['text'] == whose_char:
        return 'win'
    
def comp_move():
    '''
    Функция ходит за компьютер
    '''
    end=0
    while end==0:
        r_move = randint(0,2)
        c_move = randint(0,2)
        if field[r_move][c_move]['text'] == ' ':
            end=1
            field[r_move][c_move]['text'] = comp_char
            if check_res(comp_char) == 'win':
                end_game(comp_char)
                
def comp_move_prof():
    '''
    Функция проверяет комбинацию на выигрыш и выигрывает
    '''
    string_char = [' ', comp_char, comp_char]
        
    for r in range(3):
        if sorted(field[r][0]['text'] + field[r][1]['text'] + field[r][2]['text']) == string_char:
            if field[r][0]['text'] == ' ':
                field[r][0]['text'] = comp_char
                return 0
            elif field[r][1]['text'] == ' ':
                field[r][1]['text'] = comp_char
                return 0            
            elif field[r][2]['text'] == ' ':
                field[r][2]['text'] = comp_char
                return 0
        if sorted(field[0][r]['text'] + field[1][r]['text'] + field[2][r]['text']) == string_char:
            if field[0][r]['text'] == ' ':
                field[0][r]['text'] = comp_char
                return 0
            if field[1][r]['text'] == ' ':
                field[1][r]['text'] = comp_char
                return 0
            if field[2][r]['text'] == ' ':
                field[2][r]['text'] = comp_char
                return 0
    if sorted(field[0][0]['text'] + field[1][1]['text'] + field[2][2]['text']) == string_char:
            if field[0][0]['text'] == ' ':
                field[0][0]['text'] = comp_char
                return 0
            if field[1][1]['text'] == ' ':
                field[1][1]['text'] = comp_char
                return 0
            if field[2][2]['text'] == ' ':
                field[2][2]['text'] = comp_char
                return 0
    if sorted(field[0][2]['text'] + field[1][1]['text'] + field[2][0]['text']) == string_char:
            if field[0][2]['text'] == ' ':
                field[0][2]['text'] = comp_char
                return 0
            if field[1][1]['text'] == ' ':
                field[1][1]['text'] = comp_char
                return 0
            if field[2][0]['text'] == ' ':
                field[2][0]['text'] = comp_char
                return 0
    comp_move()
            

def click(row,col):
    '''
    Функция обрабатывает нажатие кнопок, отправляет на проверку комбинации и отдает ход компьютеру
    '''
    win=0
    if field[row][col]['text'] == ' ':
            field[row][col]['text'] = my_char 
            if check_res(my_char) == 'win':
                win=1
                end_game(my_char)
    if win == 0:
        if comp_level == "Профи":
            comp_move_prof()
            if check_res(comp_char) == 'win':
                end_game(comp_char)
        else:
            comp_move() 
    
def selected(event):
    '''
    Функция получает выделенный объект из Combobox
    '''
    global comp_level
    comp_level = drop_down.get()
    
field = []
 
root = Tk()
root.title('Крестики - нолики')

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 30, 'bold'),
                        background='lightblue',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
    
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=4, column=2, padx=10, pady=10)

level_list = ['Новичок', 'Профи']
level_list_var = StringVar(value=level_list[1])
drop_down = ttk.Combobox(root, textvariable = level_list_var, values = level_list, state="readonly")
comp_level=level_list[1]
drop_down.grid(row = 4, column = 0, columnspan=2, padx=10, pady=10)
drop_down.bind("<<ComboboxSelected>>", selected)
print(comp_level)
root.mainloop()

