import argparse
from pathlib import Path


def convert_to_dir(file: Path):
    pass


def fix_file(file: Path):
    pass


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
