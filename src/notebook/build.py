import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from typing import TextIO, Optional, Text
from time import time
import os

NB_CONFS_CODE = """import os
import sys
ROOT = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
SRC = os.path.abspath(os.path.join(ROOT, "src"))
sys.path.append(ROOT)
sys.path.append(SRC)"""


def _generate_nb_with_confs(output_path: TextIO) -> None:
    nb = new_notebook()
    nb["cells"].append(new_markdown_cell("## Confs"))
    nb["cells"].append(new_code_cell(NB_CONFS_CODE))
    with open(output_path, "w") as f:
        nbformat.write(nb, f)
        f.close()


def _nb_name(name: Optional[Text]) -> Text:
    unix_timestamp = int(time())
    if name is not None:
        return "{}-{}".format(name, unix_timestamp)
    else:
        return "notebook-{}".format(unix_timestamp)


def create_notebook(name: Optional[Text] = None) -> None:
    nb_name: str = _nb_name(name)
    nb_path = os.path.join("notebooks", nb_name + ".ipynb")
    _generate_nb_with_confs(nb_path)
