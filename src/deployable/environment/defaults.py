from typing import Dict, List # For typing

# Type id for file
file_id = "file"

# Deployment types; Always should start with a unique letter; Always must contain a file id
types: Dict[str, Dict[str, str]] = {
	file_id: {
		"name" : "file"
	},
	"string" : {
		"name": "string"
	},
	"url" : {
		"name": "URL"
	}
}