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
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Enable recursive sort"
    )
    args = parser.parse_args()
    return (args.path, args.recursive)


def find_all_files(path, directories, files):
    for directory in directories:
        _, temp_dirs, temp_files = list(os.walk(f"{path}\\{directory}"))[0]
        temp_dirs = [f"{directory}\\{temp_dir}" for temp_dir in temp_dirs]
        files.update({directory: temp_files})
        if len(temp_dirs) > 0:
            find_all_files(path, temp_dirs, files)


def main(path, recursive):

    _, directories, files = list(os.walk(path))[0]
    directories = [f"\\{directory}" for directory in directories]
    files = {"": files}

    if recursive:
        find_all_files(path, directories, files)

    extensions = {
        directory: {os.path.splitext(file)[1]: [] for file in temp_files}
        for directory, temp_files in files.items()
    }

    for directory, temp_files in files.items():
        for file in temp_files:
            name, ext = os.path.splitext(file)
            extensions[directory][ext].append(name)

    for directory, temp_extensions in extensions.items():
        for ext in temp_extensions.keys():
            dir_name = "undefined" if ext == "" else ext
            if not os.path.exists(f"{path + directory}\\{dir_name}"):
                os.mkdir(f"{path + directory}\\{dir_name}")
            for file in extensions[directory][ext]:
                os.replace(f"{path + directory}\\{file}{ext}", f"{path + directory}\\{dir_name}\\{file}{ext}")


if __name__ == '__main__':

    try:
        main(*parser())
    except Exception:
        print('An unknown error has occurred:')
        print(sys.exc_info())
