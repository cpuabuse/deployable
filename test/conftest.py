def pytest_sessionstart(session):
	"""
	Adds the source to path.
	"""
	from pathlib import Path
	from sys import path
	src_path: str = Path(__file__).parent.joinpath("../src").as_posix()
	if src_path not in path:
		path.append(src_path)