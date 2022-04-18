import click
import os
from prettytable import PrettyTable
from prettytable import from_csv
import cliapp


pt = PrettyTable()

@click.command()
@click.argument('filename')
def showtable(filename):
    nm =  os.path.join(os.path.dirname(__file__) ,'data',filename)
    print("NM",nm)
    
    with open(nm) as fd:
      pt = from_csv(fd)
      click.echo(pt)



@click.group()
def grp():
    pass

@grp.command()
@click.option('--start', default=1, help='начальная строка')
@click.option('--end', default=2, help='конечная строка')
def byrows( start,end):
    click.echo('фильтрация по строкам')
    nm =  os.path.join(os.path.dirname(__file__) ,'data','data.csv')
    
    with open(nm) as fd:
      pt = from_csv(fd)
      click.echo(pt.get_string(start = start, end = end))


@grp.command()
@click.option("--cols", '-m', 
              multiple=True, 
              default=["ФИО"],
              help="Укажите список полей, используя ключ -m. Например: showpart cols -m ФИО -m Оценка"
              )
def bycols(cols):
    click.echo('фильтрация по столбцам')
    
    nm =  os.path.join(os.path.dirname(__file__) ,'data','data.csv')
    #!!! cliapp.datafile вместо nm
    with open(cliapp.datafile) as fd:
      pt = from_csv(fd) 
      print('cols ',cols,  )
      print(pt.get_string(fields = cols))


grp.add_command(byrows)
grp.add_command(bycols)