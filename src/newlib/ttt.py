import click

def func():
    print("ttt func", __file__)


@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!???')   
    
@click.command()
def cli2():
    """Example script."""
    click.echo('Привет World!???')       