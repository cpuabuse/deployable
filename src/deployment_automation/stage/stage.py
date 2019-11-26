"""
Module containing the base stage class.
"""

from ..defaults import default_stage_name

class Stage:
	# Stage name
	name: str

	# Constructor
	def __init__(self, name: str = default_stage_name, ):
		self.name = name