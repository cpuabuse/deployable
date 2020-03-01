from deployable.run.deployment.deployment import Deployment
from pathvalidate import ValidationError, validate_filepath


class FileDeployment(Deployment):
	"""
	Provides functionality for deployment from the file.
	"""
	name = "file"

	def __init__(self):
		"""
		Constructor.
		"""
		# Call superconstructor
		super().__init__()

	@staticmethod
	def validate(filepath: str) -> bool:
		"""
		Performs a check if the string provided is file or not.
		"""
		try:
			validate_filepath(filepath)
		except ValidationError:
			return False

		return True
