"""
A package for automation of deployment to several target types.
"""

# Bootstrap to be able to perform absolute imports as standalone code
from sys import path
from pathlib import PurePath
current_path: str = PurePath(__file__).parent.parent.as_posix()
if current_path not in path:
	path.append(current_path)

# Namespace
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

# Imports
