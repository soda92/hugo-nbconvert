import argparse
from pathlib import Path
import os
import glob
import shutil


def convert_to_dir(file: Path):
    if file.stem == "index":
        print(f"{file} is already in dir structure.")
        return
    dir_name = file.stem
    dir_path = file.parent.joinpath(dir_name)
    try:
        dir_path.mkdir(exist_ok=False)
    except OSError:
        print(f"dir {dir_path} already exits.")
        return -2

    new_path = dir_path.joinpath("index" + file.suffix)
    shutil.move(file, new_path)


def fix_file(file: Path):
    pass


def fix_file_glob(glob_str: str):
    base_dir = Path(os.getcwd())
    files = glob.glob(glob_str, root_dir=base_dir, recursive=True)
    for file in files:
        file_path = base_dir.joinpath(file)
        fix_file(file_path)


def convert_to_dir_glob(glob_str: str):
    base_dir = Path(os.getcwd())
    files = glob.glob(glob_str, root_dir=base_dir, recursive=True)
    for file in files:
        file_path = base_dir.joinpath(file)
        convert_to_dir(file_path)


def get_args():
    parser = argparse.ArgumentParser(
        usage="""
a tool to add front matter to ipynb/md files.

> hugo_fix ./content/*.ipynb
        convert ipynb to dir structure and add front matter.
> hugo_fix ./docs/*.md
        add front matter to markdown files (extracting datetime from git).
> hugo_fix --to-dir/-d ./docs/aaa.md | hugo_todir ./docs/aaa.md | hugo_todir ./docs/aaa.ipynb
        convert the file to dir structure.
"""
    )

    parser.add_argument("target_file", type=str, help="file path")
    parser.add_argument(
        "--to-dir",
        "-d",
        action="store_true",
        default=False,
        help="convert the file to directory",
    )

    args = parser.parse_args()
    return args


## entry points


def to_dir_main():
    args = get_args()
    args.to_dir = True
    main(args)


def fix_main():
    args = get_args()
    main(args)


# main proc
def main(args):
    if args.to_dir:
        fix_file(args.target_file)
        convert_to_dir(args.target_file)
    else:
        fix_file(args.target_file)
