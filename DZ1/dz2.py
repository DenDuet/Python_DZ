#  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def table_of_truth():
    print("----------------------------------------")
    print(":    X    :    Y    :    Z    : Result :")
    print("----------------------------------------")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f": {str(bool(x)).ljust(5,' ')}   : {str(bool(y)).ljust(5,' ')}   : {str(bool(z)).ljust(5,' ')}   : {str((not(x or y or z)== (not (x) and not(y) and not (z)))).ljust(6,' ')} :")
    print("----------------------------------------")
                
table_of_truth()
