class Deployment:
	"""
	Class for deployment process from a deployment config.
	"""

	def __init__(self) -> None:
		"""
		Creates an instance of Deployment.
		"""

	# Validator, that fails by default
	def validate(self, id: str) -> bool:
		"""
		Dummy validator, fails by default.
		To be replaced by classes extending it.
		"""
		return False
