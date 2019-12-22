from deployable.run.deployment.deployment import Deployment
from validators import url as validate_url, ValidationFailure
from typing import Union

class UrlDeployment(Deployment):
	"""
	Provides functionality for deployment from the url.
	"""

	def __init__(self):
		"""
		Constructor.
		"""
		# Call superconstructor
		super().__init__()

	@staticmethod
	def validate(url: str) -> bool:
		"""
		Performs a check if the string provided is url or not.
		"""
		validation: Union[bool, ValidationFailure] = validate_url(url)
		if type(validation) is bool:
			return validation

		return False
