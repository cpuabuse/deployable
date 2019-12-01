"""
Module containing the base stage class.
"""

from typing import Any, Dict  # For typing

"""
Base stage class.

All of the classes extending this must provide the "run" and "dry" methods.
"""
class Stage:
	arg: str
	config: Dict[str, Any]

	# Constructor
	def __init__(self, arg: str, config: Dict[str, Any]):
		self.arg = arg
		self.config = config