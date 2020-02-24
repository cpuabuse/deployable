"""
Config types.
"""

from typing import Callable, NewType

Validator = NewType("Validator", Callable[[str], bool]) # Type for validators inside of config types


class Type():
	"""
	Base class for config types.
	"""

	def __init__(self, name: str, validator: Validator):
		name: str = name
		validator: Validator = validator
