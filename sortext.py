import os
import sys
import argparse


def parser():
    parser = argparse.ArgumentParser(
        usage=f"{os.path.basename(__file__)} [--help] [path]",
    )
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default=os.getcwd(),
        metavar="path",
        help="Directory to sort"
    )
    args = parser.parse_args()
    return args.path


def main(path):

    files = list(os.walk(path))[0][2]
    extensions = {os.path.splitext(file)[1]: [] for file in files}

    for file in files:
        name, ext = os.path.splitext(file)
        extensions[ext].append(name)

    for ext in extensions.keys():
        dir_name = "undefined" if ext == "" else ext
        os.mkdir(f"{path}\\{dir_name}")
        for file in extensions[ext]:
            os.replace(f"{path}\\{file}{ext}", f"{path}\\{dir_name}\\{file}{ext}")


if __name__ == '__main__':

    try:
        main(parser())
    except Exception:
        print('An unknown error has occurred:')
        print(sys.exc_info())
