import click

@click.command()
@click.option('--fname', prompt='Имя файла: ',  help='Укажите имя файла.')
def getfile( fname):
    """Читаем указанный файл"""
    
    with open(fname, 'r') as f:
       for s in f.readlines():
           click.echo(s)
      