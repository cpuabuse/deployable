"""
Module providing operation of the deployments.
"""
from deployable.deployment.defaults import default_work_path # For default config options
from deployable.deployment.stage.stage import Stage # For stage
from deployable.deployment.stage.echo import Echo # For stage
from deployable.report.error import report_error # Error reporting
from typing import Any, Dict, List  # For typing

"""
Class for deployment process from a deployment config.
"""
class Deployment:
	config: Dict[str, Any] = dict()
	lifecycle: bool = True
	stage: List[Stage] = list()
	

	"""
	Creates an instance of Deployment.
	"""
	def __init__(self, config: List[Dict[str, Any]], system: Dict[str, str]):
		try:
			# Initialize const
			if "const" in config:
				if type(config["const"]) is dict:
					self.config["const"] = config["const"]
				else:
					if type(config["const"]) is not None:
						raise TypeError
					config["const"] = dict()

			# Initialize option
			config["options"] = dict()
			if "options" in config:
				if type(config["options"]) is dict:
					self.config["options"] = config["options"]
				else:
					if type(config["options"]) is not None:
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
		except TypeError:
			self.lifecycle = False
			report_error("arg", "the deployment arguments failed the sanity test by type")
		except ValueError:
			self.lifecycle = False
			report_error("arg", "the deployment arguments failed the sanity test by value")	