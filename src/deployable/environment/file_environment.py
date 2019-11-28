#!/usr/bin/env python3
"""
A module creating the environment, which initializes the deployments from command line arguments.
"""

# Imports
from deployment import Deployment  # For creating deployments
from report import report_error # Error reporting
from os import getcwd  # For path resolution
from os.path import join, sep # For path resolution, and system vars
from yaml import BaseLoader, load # To convert yaml to dict 
from typing import Dict, List  # For typing

"""
Class for specifying the environment of operation.
"""
class Environment:
	# Array of deployments
	deployment: List[Deployment] = list()
	system: Dict[str, str] = {
		sep: sep
	}

	"""
	Parses and return the command line arguments.
	"""
	def __init__(self):
		# Default config file name
		global default_config_path

	

		# Create deployments
		try:
			for config_path in args.config:
				with open(config_path) as config_file:
					self.deployment.append(Deployment(config_path, load(config_file, Loader=BaseLoader), self.system))
		except OSError:
			report_error("io", config_path)
		except [TypeError, ValueError]:
			report_error("parsing", config_path)

