import click


@click.command()
def cli():
    """Простой пример 1"""
    click.echo('Hello World!!!')   
    
@click.command()
def cli2():
    """Простой пример 2"""
    click.echo('Привет Мир!')       