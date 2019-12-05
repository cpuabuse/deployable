"""
Module for error handling.
"""
from deployable.report.defaults import error_break, error_list, error_label # Error messages and so on
from sys import stderr # stderr

"""
Reports an error.
"""
def report_error(code: str, message: str):
	try:
		print(error_label + error_list[code] + error_break + message, file=stderr)
	except:
		print(error_label + error_list["error"])