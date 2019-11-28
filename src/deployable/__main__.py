"""
Main module for the deployable project.
"""

# Bootstrap to be able to perform absolute imports as standalone code
if __name__ == "__main__":
	from sys import path
	from pathlib import PurePath
	current_path: str = PurePath(__file__).parent.parent.as_posix()
	if current_path not in path:
		path.append(current_path)

from argparse import ArgumentParser, Namespace  # For parsing arguments
from defaults import default_config_path # For using the default value in Environment creation
from deployable.environment.file_environment import FileEnvironment # For creating of environment
from typing import Any, List, Tuple  # For typing

"""
Retrieves arguments from command line.
"""
def get_args() -> tuple:
	# Create parser
	parser = ArgumentParser(description='Arguments for deployment-automation.')

	# Add arguments
	parser.add_argument("-c", "--config", nargs="*", type=str, help="location of the configuration file(s)", default=[default_config_path])
	parser.add_argument("-d", "--dry", help="if specified, the stages would not execute, only evaluate the directives", default=False, action="store_true")
	
	# Generate the args object
	args = parser.parse_args()

	return args.config, args.dry
"""
Entrypoint.
"""
def main() -> None:
	# Get command line args
	config: List(str)
	dry: bool
	config, dry = get_args()

	# Create an environment
	env = FileEnvironment()
	print(env)

# Call main method
if __name__ == "__main__":
	main()