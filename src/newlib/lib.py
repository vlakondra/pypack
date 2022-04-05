'''
Библиотечный модуль
'''
from prettytable import PrettyTable

def func(n):
    print('func!!!')
    return(n**3)
def func2(n):
    print('func2!!!')
    return(n**2) 

def print_table():
    '''
     Распечатывает таблицу
    '''
    x = PrettyTable()
    x.field_names = ["Имя", "Возраст", "Рост"]
    x.add_row(["Иван", 22, 178])
    x.add_row(["Петр", 21, 182])
    x.add_row(["Сидор", 20, 160])
    print(x)
       