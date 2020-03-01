"""
Generic deployment information.
"""

from typing import List
from deployable.run.deployment.file_deployment import FileDeployment
from deployable.run.deployment.string_deployment import StringDeployment
from deployable.run.deployment.url_deployment import URLDeployment


class Deployment:
	"""
	Class for deployment process from a deployment config.
	"""

	def __init__(self) -> None:
		"""
		Creates an instance of Deployment.
		"""

	# Validator, that fails by default
	@staticmethod
	def validate(id: str) -> bool:
		"""
		Dummy validator, fails by default.
		To be replaced by classes extending it.
		"""
		return False


deployment_types: List[Deployment] = [FileDeployment, StringDeployment, URLDeployment]
