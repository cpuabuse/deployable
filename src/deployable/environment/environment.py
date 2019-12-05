"""
Provides the environment base class specification.
"""

from deployable.deployment.deployment import Deployment  # For creating deployments
from deployable.report.error import report_error # For error reporting
from typing import Any, Dict, List  # For typing

class Environment:
	# Contains deployments
	deployment: List[Deployment] = list()
	
	# Lifecycle of the environment
	lifecycle: bool = True

	# Contains system information
	system: Dict[str, str]

	"""
	Constructor.
	"""
	def __init__(self, config: List[Dict[str, Any]], environment_path: str):
		# Arguments sanity check
		if type(environment_path) is not str or type(config) is not list:
			self.lifecycle = False
			report_error("arg", "the environment arguments failed the sanity test")
			return

		# Assign system properties
		self.system.append({
			"environment_path": environment_path
		})

		# Create deployments
		for config_item in config:
			self.deployment.append(Deployment(config=config_item, system=self.system))