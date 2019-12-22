from deployable.run.deployment.deployment import Deployment
from yaml import BaseLoader, load, YAMLError

class StringDeployment(Deployment):
	"""
	Provides functionality for deployment from the string.
	"""

	def __init__(self):
		"""
		Constructor.
		"""
		# Call superconstructor
		super().__init__()

	@staticmethod
	def validate(text: str) -> bool:
		"""
		Performs a check if the string provided is yaml string or not.
		"""
		try:
			string_type: type = type(load(text, Loader=BaseLoader))
			if (string_type is dict):
				return True
		except YAMLError:
			pass
		return False
