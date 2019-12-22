from deployable.run.deployment.deployment import Deployment
from deployable.run.deployment.string_deployment import StringDeployment
from deployable.run.deployment.url_deployment import UrlDeployment

valid_filepath = "./"
valid_string = "hello: world"
valid_url = "https://www.example.com/resource"

class TestDeployment:
	"""
	Test Deployment class.
	"""
	def test_validator(self):
		"""
		Test validator.
		"""
		assert not Deployment.validate(valid_filepath)
		assert not Deployment.validate(valid_string)
		assert not Deployment.validate(valid_url)

class TestStringDeployment:
	"""
	Test StringDeployment class.
	"""
	def test_validator(self):
		"""
		Test validator.
		"""
		assert StringDeployment.validate(valid_string)
		assert not StringDeployment.validate(valid_filepath)
		assert not StringDeployment.validate(valid_url)

class TestUrlDeployment:
	"""
	Test UrlDeployment class.
	"""
	def test_validator(self):
		"""
		Test validator.
		"""
		assert UrlDeployment.validate(valid_url)
		assert not UrlDeployment.validate(valid_filepath)
		assert not UrlDeployment.validate(valid_string)