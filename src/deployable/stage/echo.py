"""
Stage printing a message to console.
"""

from stage import Stage # To extend
from typing import Any, Dict # or typing

class Echo(Stage):
	def __init__(self, arg: str, config: Dict[str, Any]):
		# Call superconstructor
		super().__init__(arg, config)

	def execute(self):
		print(self.arg)