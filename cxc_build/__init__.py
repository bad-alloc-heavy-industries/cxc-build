# SPDX-License-Identifier: BSD-3-Clause
try:
	try:
		from importlib import metadata as importlib_metadata # py3.8
	except ImportError:
		import importlib_metadata # py3.7
	__version__ = importlib_metadata.version(__package__)
except ImportError:
	__version__ = ':nya_confused:' # :nocov:

__all__ = (
	'main',
)

def main():
	import sys
	from os import path, mkdir
	from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

	parser = ArgumentParser(formatter_class = ArgumentDefaultsHelpFormatter, description = 'cxc-build')


	args = parser.parse_args()

	if not path.exists(args.build_dir):
		mkdir(args.build_dir)


	return 0
