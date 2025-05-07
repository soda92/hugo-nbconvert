from hugo_nbconvert.main import main as nbconvert
from hugo_nbconvert.new import main as hugo_new
import os

submodule = os.environ["submodule"]

if submodule == "hugo_nbconvert":
    nbconvert()
elif submodule == "hugo_new":
    hugo_new()
