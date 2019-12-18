"""
Module containing the base stage class.
"""

from typing import Any, Dict  # For typing

class Stage:
	"""
	Base stage class.
	All of the classes extending this must provide the "run" and "dry" methods.
	"""
	arg: str
	config: Dict[str, Any]

	# Constructor
	def __init__(self, arg: str, config: Dict[str, Any]) -> None:
		self.arg = arg
		self.config = config