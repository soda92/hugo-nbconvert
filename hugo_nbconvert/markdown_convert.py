from .collapse_postprocessor import CollapsePostprocessor
from sodatools import Path
import subprocess


def convert_proc(conf_path: Path, file: Path):
    subprocess.run(
        ["jupyter", "nbconvert", "--config", conf_path, "--to", "markdown", file]
    )
    output_filepath = file.with_suffix(".md")
    if output_filepath.exists():
        postprocessor = CollapsePostprocessor(output_filepath)
        postprocessor.process()
