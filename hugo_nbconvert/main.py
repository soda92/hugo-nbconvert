import subprocess
from hugo_nbconvert.glob_hugo_ipynb import get_files


def main():
    files = get_files()
    for i in files:
        subprocess.run(["jupyter", "nbconvert", "--to", "markdown", i])


if __name__ == "__main__":
    main()
