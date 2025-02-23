import click
import os
from helper import is_utf8

@click.group()
def cli():
    pass

@click.command()
@click.option('-c', is_flag=True, help="outputs the number of bytes in a file")
@click.option('-l', is_flag=True, help="outputs the number of lines in a file")
@click.option('-w', is_flag=True, help="outputs the number of words in a file")
@click.argument('filename')
def wc(c, l, w, filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return
    if not is_utf8(filename):
            print(f"Error: File '{filename}' is not UTF-8 encoded.")
            return
    if c:
        print(os.path.getsize(filename), filename)
    if l:
        with open(filename, "r", encoding="utf-8") as f:
            num_lines = sum(1 for line in f)
        print(num_lines, filename)
    if w:
        with open(filename, "r", encoding="utf-8") as f:
            num_words = sum(len(line.split()) for line in f)
        print(num_words, filename)

cli.add_command(wc)

if __name__ == '__main__':
    cli()