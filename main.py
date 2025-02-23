import click
import os

@click.group()
def cli():
    pass

@click.command()
@click.option('-c', is_flag=True, help="outputs the number of bytes in a file")
@click.argument('filename')
def wc(c, filename):
    if(c):
        print(os.path.getsize(filename), filename)

cli.add_command(wc)

if __name__ == '__main__':
    cli()