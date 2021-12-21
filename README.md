<h1 align="center">Sortext</h1>

<p align="center">The CLI script created with Python to sort files by their extensions</p>

<p  align="center">
	<a style="text-decoration:none" href="https://github.com/TheFifthLeaf/sortext/releases">
		<img src="https://img.shields.io/github/v/release/TheFifthLeaf/sortext?color=3C7DD9" alt="Releases">
	</a>
	<a style="text-decoration:none" href="https://www.python.org/downloads/">
		<img src="https://img.shields.io/badge/python-3.6%2B-3C7DD9" alt="Python Version">
	</a>
	<a style="text-decoration:none" href="https://choosealicense.com/licenses/gpl-3.0/">
		<img src="https://img.shields.io/badge/license-GPL%20V3-3C7DD9" alt="License GPLv3">
	</a>
	<a href="https://www.codefactor.io/repository/github/thefifthleaf/sortext">
		<img src="https://img.shields.io/codefactor/grade/github/TheFifthLeaf/sortext/main?color=3C7DD9" alt="CodeFactor" />
	</a>
</p>

## Installation

This program uses only the standard Python 3 library, so installing additional modules is not necessary.

## Usage

To sort using .exe, please type:

```bash
sortext [--help] [path [--recursive] [--only <list>] [--without <list>]]
```

And using .py, type:

```bash
python sortext.py [--help] [path [--recursive] [--only <list>] [--without <list>]]
```

### Usage example

This will display help information. You can also use short "-h".
```bash
sortext --help
```
This will sort all files in specified directory by extensions.
```bash
sortext "D\MyFiles"
```
This will sort all files in nested directories. You can also use short "-r".
```bash
sortext "D\MyFiles" --recursive
```
This will sort only files with specified extensions. You can also use short "-o".
```bash
sortext "D\MyFiles" --only png jpg
```
This will sort only files without specified extensions. You can also use short "-w".
```bash
sortext "D\MyFiles" --without txt
```
You can also specify files without any extension.
```bash
sortext "D\MyFiles" --only ""
sortext "D\MyFiles" --without ""
```

## Contributing

Pull requests are welcome.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)