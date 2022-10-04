x = 0
y = 0

def init_compl(ad, am, bd, bm):
    global x
    global y
    x = complex(ad, am)
    y = complex(bd, bm)

def init_ratio(a, b):
    global x
    global y
    x = float(a)
    y = float(b)

def sum():
    return x + y

def sub():
    return x - y

def mult():
    return x * y

def div():
    if y == 0:
        return 'Деление на 0 невозможно!'
    else:
        return x / y 
