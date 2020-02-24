"""
String config type.
"""

from deployable.config._type import Type


class String(Type):
	"""
	Class for a string config type.
	"""

	def __init__(self):
		"""
		Constructor.
		"""

		def validator(text: str) -> bool:
			"""
			Validates a string.
			"""

			try:
				string_type: type = type(load(text, Loader=BaseLoader))
				if (string_type == dict):
					return True
			except:
				pass
			return False

		super().__init__(name="File", validator=validator)
