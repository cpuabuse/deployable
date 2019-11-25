#!/usr/bin/env python3
"""
A module creating the environment, which initializes the deployments from command line arguments.
"""

# Imports
from argparse import ArgumentParser, Namespace  # For parsing arguments
from defaults import default_config_path # For using the default value in Environment creation
from deployment import Deployment  # For creating deployments
from os import getcwd  # For path resolution
from os.path import join # For path resolution
from typing import List  # For typing

"""
Class for specifying the environment of operation.
"""
class Environment:
	# Array of deployments
	deployment: List[Deployment] = list()

	"""
	Parses and return the command line arguments.
	"""
	def __init__(self):
		# Default config file name
		global default_config_path

		# Create parser
		parser = ArgumentParser(description='Arguments for deployment-automation.')

		# Add arguments
		parser.add_argument("-c", "--config", nargs="*", type=str, help="location of the configuration file(s)", default=[default_config_path])
		
		# Generate the args object
		args = parser.parse_args()

		# Create deployments
		for config_path in args.config:
			self.deployment.append(Deployment(config_path,config_path))

"""
Entrypoint.
"""
def main() -> None:
	# Create an environment
	env = Environment()

if __name__ == "__main__":
	main()