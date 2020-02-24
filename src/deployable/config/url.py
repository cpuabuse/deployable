"""
File config type.
"""

from deployable.config._type import Type
from requests.exceptions import MissingSchema
from requests.models import PreparedRequest


class URL(Type):
	"""
	Class for a file config type.
	"""

	def __init__(self):
		"""
		Constructor.
		"""

		def validator(text: str) -> bool:
			"""
			Validates a URL.
			"""

			prepared_request = PreparedRequest()
			try:
				prepared_request.prepare_url(text, None)
				return True
			except MissingSchema:
				return False

		super().__init__(name="File", validator=validator)
