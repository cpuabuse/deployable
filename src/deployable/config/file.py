"""
File config type.
"""

from deployable.config._type import Type


class File(Type):
	"""
	Class for a file config type.
	"""

	def __init__(self):
		"""
		Constructor.
		"""

		def validator(text: str) -> bool:
			"""
			Validates wether the text is a file.
			"""

			try:
				Path(text).resolve(strict=True)
				return True
			except:
				return False

		super().__init__(name="File", validator=validator)
