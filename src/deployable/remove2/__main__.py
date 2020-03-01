#!/usr/bin/env python3

"""
Main module for the deployable project.
"""

# Shared imports for bootstrap and normal use
from pathlib import Path  # For bootstrap and figuring out paths from args

# Bootstrap to be able to perform absolute imports as standalone code
if __name__ == "__main__":
	from absolute_import import absolute_import
	absolute_import(file=__file__, name=__name__, path=__path__)

from typing import Any, List, Optional, Set, Tuple
from deployable.environment.file_environment import FileEnvironment
from deployable.environment.defaults import file_id, types
from deployable.defaults import description, epilog, get_help
from deployable.defaults import default_config_path, default_environment_path
from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter


# Normal imports


def get_args() -> Tuple[Any]:
	"""
	Retrieves arguments from command line.
	"""
	# Create parser and groups
	parser = ArgumentParser(description=description, epilog=epilog,
                         formatter_class=RawDescriptionHelpFormatter)

	# Add type overrides
	type_override_group = parser.add_mutually_exclusive_group()
	# The default value is required for "*" nargs to work with mutual exlusion
	type_override_group.add_argument(
		"-t", "--type", choices=[type_item for type_item in types], default=None, help=get_help("type"), nargs="*")
	for type_item in types:
		type_override_group.add_argument(
			f"-{type_item[0]}", f"--{type_item}", action="store_true", default=False, help=get_help(type_item))

	# Add normal arguments
	parser.add_argument("-c", "--config", nargs="*", type=str,
                     help=get_help("config"), default=[default_config_path])
	parser.add_argument("-d", "--dry", help=get_help("dry"),
                     default=False, action="store_true")
	parser.add_argument("-e", "--environment", type=str,
                     help=get_help("environment"))

	# Generate the args object
	args = parser.parse_args()

	# Deal with types
	arg_type: List[str] = [file_id] * len(args.config)
	if args.type != parser.get_default("type"):
		for i in range(min(len(args.type), len(args.config))):
			arg_type[i] = args.type[i]
	force_types: List[str] = [
		type_item for type_item in types if getattr(args, type_item) == True]
	if len(force_types) == 1:
		for i in range(len(arg_type)):
			arg_type[i] = force_types[0]
	else:
		# Perform type guessing
		for i in range(len(arg_type)):
			arg_type[i] = guess_type(args.config[i])

	# Determine environment
	environment: str = None
	if args.environment == parser.get_default("environment"):
		environment = default_environment_path
		config_set: Set[str] = set(
			[Path(args.config[i]).parent.as_posix() for i in range(len(arg_type))])
		if len(config_set) == 1:
			environment = config_set.pop()
	else:
		environment = args.environment

	# Return the args
	return args.config, args.dry, environment, arg_type


def guess_type(text: str) -> Optional[str]:
	"""
	Guesses the type of the string.
	Performs the check for file the last.
	"""
	for type_item in types:
		if type_item != file_id:
			if types[type_item]["validator"](text):
				return type_item
	if types[file_id]["validator"](text):
		return file_id
	else:
		return None


def main() -> None:
	"""
	Entrypoint.
	"""
	# Get command line args
	config: List(str)
	dry: bool
	env_path: str
	config_type: List(str)
	config, dry, env_path, config_type = get_args()

	print("Debug: exiting")


# Call main method
if __name__ == "__main__":
	main()
