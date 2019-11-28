"""
Module providing operation of the deployments.
"""

from defaults import default_work_path # For Deployment construction
from report import report_error # Error reporting
from echo import Echo # For stage
from stage import Stage
from typing import Any, Dict, List  # For typing

"""
Class for deployment process from a deployment config.
"""
class Deployment:
	stage: List(Stage) = list()
	config: Dict[str, Any]

	"""
	Creates an instance of Deployment.
	"""
	def __init__(self, root_path: str, config: List[Dict[str, Any]], system: Dict[str, str]):
		# Initialize const
		if "const" in config:
			if type(config["const"]) is dict:
				self.config["const"] = config["const"]
			else:
				if type(config["const"]) is not None:
					raise TypeError
				config["const"] = dict()

		# Initialize option
		config["option"] = dict()
		if "option" in config:
			if type(config["option"]) is dict:
				self.config["option"] = config["option"]
			else:
				if type(config["option"]) is not None:
					raise TypeError
		if "work_dir" not in self.config["options"]:
			self.config["options"]["work_dir"] = default_work_path
		
		# Initialize arg
		if "arg" in config:
			if type(config["arg"]) is dict:
				self.config["arg"] = config["arg"]
			else:
				if type(config["arg"]) is not None:
					raise TypeError
				config["arg"] = dict()

		# Initialize var
		if "var" in config:
			if type(config["var"]) is dict:
				self.config["var"] = config["var"]
			else:
				if type(config["var"]) is not None:
					raise TypeError
				config["var"] = dict()

		# Initialize var
		if "alias" in config:
			if type(config["alias"]) is list:
				self.config["alias"] = config["alias"]
			else:
				if type(config["alias"]) is not None:
					raise TypeError
				config["alias"] = dict()

		# Initialize system
		self.config["system"] = system

		# Create stage
		if "stage" in config:
			if type(config["stage"]) is list:
				for stage in config:
					# Verify the consistency of data to satisfy the stage
					if type(stage) is not dict:
						raise TypeError

				# Append to self
				self.stage.append(Stage(stage["echo"]))
			else:
				raise TypeError
		else:
			raise ValueError
