import glob
from pathlib import Path
CR = Path(__file__).resolve().parent

def test_glob():
    filename = './test_glob_full_path.py'
    r = glob.glob(filename, recursive=True, root_dir=CR)

    assert len(r) == 1
    assert CR.joinpath(filename).exists()