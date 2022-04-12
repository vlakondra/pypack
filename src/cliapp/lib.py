'''
Библиотечный модуль
'''
from prettytable import PrettyTable

# from src.newlib import CONST_PI # NOT OK
from cliapp import CONST_PI as PI #OK


def func(n):
    print('func!!!',  PI)
    return(n**3)

def scircle(r):
    return(PI * r ** 2) 

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
       
if __name__ == "__main__":
    func(33)       