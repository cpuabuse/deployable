"""
Module providing operation of the deployments.
"""

from error import report_error # Error reporting
from typing import Dict, List, Union  # For typing

"""
Class for deployment process from a deployment config.
"""
class Deployment:
	stage: List[Dict[str, Union[int, str]]] = list()

	"""
	Creates an instance of Deployment.
	"""
	def __init__(self, root_path: str, config: List[Dict[str, Union[int, str]]]):
		for stage in config:
			# Verify the consistency of data to satisfy the stage
			if type(stage) is not dict:
				raise TypeError
			if "name" in stage:
				if type(stage["name"]) is not str:
					raise TypeError

			# Append to self
			self.stage.append(stage)