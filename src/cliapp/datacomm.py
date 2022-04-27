import click
import os
from prettytable import PrettyTable
from prettytable import from_csv
import cliapp

pt = PrettyTable()

#https://stackoverflow.com/questions/46550523/passing-class-instance-through-context

class Data(object):
    def __init__(self, path = None):
        self.pathdata = os.path.abspath(path) 

# pass_repo = click.make_pass_decorator(Data)

@click.group(invoke_without_command=True)
@click.option('--filename','-f', 
              required=False,
              type=click.Path(exists=True),
              help="Путь к файлу данных")
@click.pass_context
def grp(ctx, filename):
    
    grp_commands = ['show', 'info']
    
    if ctx.invoked_subcommand is None:
        print()
        click.echo("Укажите путь к файлу данных ")
        click.echo("и выберите одну из этих команд:")
        print(*grp_commands, sep='\n')
        print()
   
    if filename:
      ctx.obj = Data(filename)  


# print('repo', pass_repo, pass_repo.__str__())


@grp.command('show', help='Показать данные') 
@click.option('--color', '-c', help="Укажите цвет")
@click.pass_obj
# @click.make_pass_decorator(Data)
def showdata(obj, color):
  if obj.pathdata:
    with open(obj.pathdata) as fd:
      prt = from_csv(fd)
      click.secho(prt, fg=color)

###################################

@grp.command('info', help="Показать информацию о таблице") 
@click.pass_obj 
def showinfo(obj):
   if obj.pathdata:
    with open(obj.pathdata) as fd:
     ln = fd.readlines()
     print(len(ln))
     cols= ln[0].split(',')
     print( len(cols))


# @grp.command("rows")
# @click.option('--start', default=1, help='укажите индекс начальной строки')
# @click.option('--end', default=2, help='укажите индекс конечной строки')
# @click.pass_obj
# def byrows(ctx, start,end):
#     click.echo('фильтрация по строкам')

#     with open(ctx['filename']) as fd:
#       pt = from_csv(fd)
#       click.echo(pt.get_string(start = start, end = end))

# print(grp.__dict__)

# grp.add_command(showdata)
# grp.add_command(showinfo)

# print(grp.__dict__)