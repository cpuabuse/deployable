#!/usr/bin/env python3
"""
A module creating the environment, which initializes the deployments from command line arguments.
"""

# Imports
from deployable.environment.environment import Environment # For class extension
from deployable.report.error import report_error # Error reporting
from os.path import join, sep # For path resolution, and system vars
from typing import Any, List, Dict # For typing
from yaml import BaseLoader, load # To convert yaml to dict 


class FileEnvironment(Environment):
	"""
	Class for specifying the environment of operation.
	"""
	def __init__(self, config: List[str], environment_path: str):
		"""
		Parses and return the command line arguments.
		"""
		# Sanity check
		if type(config) is list:
			if len(config) > 0:
				config_data_set = False
				
				try:
					config_data = map(path_to_object, config)
					config_data_set = True
				except OSError:
					report_error("io", "file probably does not exist")
				except [TypeError, ValueError]:
					report_error("parsing", "yaml syntax is probably incorrect")
				
				if config_data_set:
					# Call superconstructor
					super().__init__(config=config_data, environment_path=environment_path)
					
					# Return to terminate finidshing up of sanity check
					return

		# If sanity check failed
		self.lifecycle = False
		report_error("arg", "the file environment arguments failed the sanity test")
		return

def path_to_object(config_path: str) -> Dict[str, Dict[str, Any]]:
	"""
	Loads yaml from a file.
	"""
	with open(config_path) as config_file:
		return load(config_file, Loader=BaseLoader)
