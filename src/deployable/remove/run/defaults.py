from pathlib import Path # For figuring out the path
from requests.exceptions import MissingSchema # For guessing the type
from requests.models import PreparedRequest # For guessing the type
from typing import Dict, List  # For typing
from yaml import BaseLoader, load  # To convert yaml to dict

# Type id for file
file_id = "file"

def validate_file(text: str):
	"""
	Validates a file.
	"""
	try:
		Path(text).resolve(strict=True)
		return True
	except:
		return False

def validate_string(text: str):
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

def validate_url(text: str):
	"""
	Validates a URL.
	"""
	prepared_request = PreparedRequest()
	try:
		prepared_request.prepare_url(text, None)
		return True
	except MissingSchema:
		return False

# Deployment types; Always should start with a unique letter; Always must contain a file id
types: Dict[str, Dict[str, str]] = {
	file_id: {
		"name": "file",
		"validator": validate_file
	},
	"string" : {
		"name": "string",
		"validator": validate_string
	},
	"url" : {
		"name": "URL",
		"validator": validate_url
	}
}