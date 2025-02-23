import click
import os
import sys
from helper import is_utf8

@click.group()
def cli():
    pass

@click.command()
@click.option('-c', is_flag=True, help="outputs the number of bytes in a file")
@click.option('-l', is_flag=True, help="outputs the number of lines in a file")
@click.option('-w', is_flag=True, help="outputs the number of words in a file")
@click.option('-m', is_flag=True, help="outputs the number of characters in a file")
@click.argument('file', required=False)
def wc(c, l, w, m, file):
    # If no options are provided, default to -c, -l, -w
    if not (c or l or w or m):
        c, l, w = True, True, True

    # Read from standard input if no file is given
    if file:
        if not os.path.exists(file):
            print(f"Error: File '{file}' not found.", file=sys.stderr)
            return
        input_source = open(file, "r", encoding="utf-8")
    else:
        input_source = sys.stdin

    with input_source as f:
        content = f.read()
        
        num_bytes = os.path.getsize(file) if file else len(content.encode())
        lines = content.splitlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = len(content)

        output_parts = []
        if c:
            output_parts.append(f"{num_bytes}")
        if l:
            output_parts.append(f"{num_lines}")
        if w:
            output_parts.append(f"{num_words}")
        if m:
            output_parts.append(f"{num_chars}")

        # Print the formatted output with optional file
        print(" ".join(output_parts), file if file else "")

cli.add_command(wc)

if __name__ == '__main__':
    cli()