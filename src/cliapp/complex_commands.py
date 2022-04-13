import click
import os
import  importlib.resources as ir
import cliapp

@click.command()
@click.option('--fname', prompt='Имя файла: ',  help='Укажите имя файла.')
def getfile( fname):
    """Читаем указанный файл"""
    print('file',os.path.dirname(__file__))
    print(os.getcwd(),__file__)
    f= ir.open_text(package=cliapp, resource='file.txt', encoding="utf-8")
    res= f.read()
    print('res\n',res, sep='\n')
    
    nm =  os.path.join(os.path.dirname(__file__) ,fname)
    with open(nm, 'r') as f:
       for s in f.readlines():
           click.echo(s)
      
      
@click.command()
@click.argument('filename', type=click.Path(exists=True))
def touch(filename):
    """Print FILENAME if the file exists."""
    nm =  os.path.join(os.path.dirname(__file__) ,filename)
    click.echo(click.format_filename(nm))      