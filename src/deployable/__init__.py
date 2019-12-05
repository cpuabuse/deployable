"""
A package for automation of deployment to several target types.
"""

# Bootstrap to be able to perform absolute imports as standalone code
from pathlib import Path
from sys import path
current_path: str = Path(__file__).parent.joinpath("..").as_posix()
if current_path not in path:
	path.append(current_path)

# Namespace
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)