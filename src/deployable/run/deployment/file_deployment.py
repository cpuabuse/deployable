from deployable.run.deployment.deployment import Deployment

class FileDeployment(Deployment):
	"""
	Provides functionality for deployment from the file.
	"""
	def __init__(self):
		"""
		Constructor.
		"""
		# Call superconstructor
		super().__init__()

	def validate(self, id: str) -> bool:
		"""
		Performs a check if the string provided is file or not.
		"""
		return False