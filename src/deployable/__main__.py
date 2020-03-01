#!/usr/bin/env python3

"""
Main module for the deployable project.
"""

# Bootstrap to be able to perform absolute imports as standalone code
if __name__ == "__main__":
	from absolute_import import absolute_import
	absolute_import(file=__file__, name=__name__, path=__path__)

# Normal imports
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from deployable.defaults.args import description, epilog
from typing import Any, Tuple


def get_args() -> Tuple[Any]:
	"""
	Retrieves arguments from command line.
	"""
	# Create parser and groups
	parser = ArgumentParser(description=description, epilog=epilog, formatter_class=RawDescriptionHelpFormatter)


def main() -> None:
	"""
	Entrypoint.
	"""


# Call main method
if __name__ == "__main__":
	main()
