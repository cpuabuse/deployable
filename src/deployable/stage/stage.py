"""
Module containing the base stage class.
"""

from ..deployment import default_stage_name
from typing import Any, Dict  # For typing

class Stage:
	arg: str
	config: Dict[str, Any]

	# Constructor
	def __init__(self, arg: str, config: Dict[str, Any]):
		self.arg = arg
		self.config = config