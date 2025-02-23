# wc\_cli\_tool

A command-line utility similar to Unix `wc`, written in Python using Click.

## Features

- Count the number of **bytes, lines, words, and characters** in a file.
- Read from **standard input** if no file is specified.
- Default behavior outputs **bytes, lines, and words** when no flags are provided.
- Supports UTF-8 encoded files.

## Installation

### Download the Repository

```sh
git clone https://github.com/NehalH/wc-cli-tool.git
cd wc-cli-tool
```

### Using pip

```sh
pip install .
```

### Using setup.py

```sh
python setup.py install
```

## Usage

### Count bytes (-c), lines (-l), words (-w), and characters (-m)

```sh
cliwc -c -l -w -m filename.txt
```

### Default (bytes, lines, words)

```sh
cliwc filename.txt
```

### Read from standard input

```sh
cat filename.txt | cliwc -l
```

### Help

```sh
cliwc --help
```

## Examples

### Count lines in a file

```sh
cliwc -l test.txt
# Output: 7145 test.txt
```

### Count words in a file

```sh
cliwc -w test.txt
# Output: 50023 test.txt
```

### Count everything (default behavior)

```sh
cliwc test.txt
# Output: 120000 7145 50023 test.txt
```

## Development

If modifying the tool, install dependencies with:

```sh
pip install -r requirements.txt
```

For editable installation:

```sh
pip install --editable .
```

##

