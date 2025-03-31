def division_function(x,y):
    try: 
        result = x // y
        print(result)
    except ZeroDivisionError:
        print("Wir dürfen nicht durch 0 teilen. Bitte gib eine andere Zahl ein, mit der wir teilen wollen")

first_number = int(input("Bitte gib eine erste Zahl ein, von der geteilt werden soll: "))
second_number = int(input("Bitte gib eine zweite Zahl ein, mit der wir teilen wollen: "))
division_function(first_number, second_number)
