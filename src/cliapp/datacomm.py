import csv
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
def rows( start,end):
    click.echo('фильтрация по строкам')
    nm =  os.path.join(os.path.dirname(__file__) ,'data','data.csv')
    
    with open(nm) as fd:
      pt = from_csv(fd)
      click.echo(pt.get_string(start=start, end=end))

@grp.command()
@click.option('--cols',  help="Укажите список полей через запятую")
def cols(cols):
    click.echo('фильтрация по столбцам')
    nm =  os.path.join(os.path.dirname(__file__) ,'data','data.csv')
    #!!! cliapp.datafile вместо nm
    with open(cliapp.datafile) as fd:
      pt = from_csv(fd)
      print('cols ',list(cols.split(' ')) )
      print(pt.get_string(fields=list(cols.split(','))))


grp.add_command(rows)
grp.add_command(cols)