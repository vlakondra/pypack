import click
import os
from prettytable import PrettyTable
from prettytable import from_csv
import cliapp


pt = PrettyTable()

def dec_fact(extn):
  def dec(f):
    def wrp(*arg,**kwargs):
      print('arg', arg,kwargs)
      fn,ext = os.path.splitext(kwargs['filename'])
      print('ext',fn ,ext)
      if not ext==extn: #'.csv':
        print('NOT OK')
        return
      f(**kwargs)
    return wrp  
  return dec




@click.command()
@click.argument('filename')
# @dec_fact('.csv')
def showtable(filename):
    # nm =  os.path.join(os.path.dirname(__file__) ,'data',filename)
    nm =  os.path.join(os.getcwd(), 'data', filename)
    
    with open(nm) as fd:
      pt = from_csv(fd)
      click.echo(pt)


@click.group()
@click.option('--fname',  default='data.csv')
@click.pass_context
def grp(ctx,fname):
    print("CTX", ctx.obj)

    ctx.obj = {'filename' :  os.path.join(os.getcwd(), 'data',fname)}


@grp.command()
@click.pass_obj
def table(obj):
    
    with open(obj['filename']) as fd:
      pt = from_csv(fd)
      click.secho(pt,fg="blue")


@grp.command("выбрать строки")
@click.option('--start', default=1, help='укажите индекс начальной строки')
@click.option('--end', default=2, help='укажите индекс конечной строки')
@click.pass_obj
def byrows(ctx, start,end):
    click.echo('фильтрация по строкам')

    with open(ctx['filename']) as fd:
      pt = from_csv(fd)
      click.echo(pt.get_string(start = start, end = end))


@grp.command("выбрать столбцы")
@click.option("--cols", '-c', 
              multiple=True, 
              default=["ФИО"],
              help="Укажите список полей, используя ключ -m. Например:  -m ФИО -m Оценка"
              )
@click.pass_obj
def bycols(ctx,cols):
    click.echo('фильтрация по столбцам')
    
    # nm =  os.path.join(os.path.dirname(__file__) ,'data','data.csv')

    with open(ctx['filename']) as fd:
      pt = from_csv(fd) 
      print('cols ',cols,  )
      print(pt.get_string(fields = cols))


grp.add_command(byrows)
grp.add_command(bycols)