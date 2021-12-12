# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup, find_packages

def vcs_ver():
	def scheme(version):
		if version.tag and not version.distance:
			return version.format_with("")
		else:
			return version.format_choice("+{node}", "+{node}.dirty")
	return {
		"relative_to": __file__,
		"version_scheme": "guess-next-dev",
		"local_scheme": scheme
	}

def doc_ver():
	try:
		from setuptools_scm.git import parse as parse_git
	except ImportError:
		return ""

	git = parse_git(".")
	if not git:
		return ""
	elif git.exact:
		return git.format_with("{tag}")
	else:
		return "latest"

setup(
	name = 'cxc-build',
	use_scm_version = vcs_ver(),
	author          = 'Aki \'lethalbit\' Van Ness',
	author_email    = 'nya@catgirl.link',
	description     = 'Cross Compiler batch build script',
	license         = 'BSD-3-Clause',
	python_requires = '>=3.8,<3.10',
	zip_safe        = False,

	setup_requires  = [
		'wheel',
		'setuptools',
		'setuptools_scm'
	],

	install_requires = [
		'Jinja2',
		'requests',
	],

	packages = find_packages(),

	package_data = {
		'cxc_build.data': [
			'common.json',
		],
		'cxc_build.data.architectures': [
			'aarch64.json',
			'alpha.json',
			'arm.json',
			'avr.json',
			'frv.json',
			'hppa1.1.json',
			'hppa2.0.json',
			'hppa64.json',
			'hppa.json',
			'ia64.json',
			'lm32.json',
			'm68k.json',
			'microblaze.json',
			'mips64.json',
			'mips.json',
			'or1k.json',
			'ppc64.json',
			'ppc64le.json',
			'ppc.json',
			'ppcle.json',
			'riscv32.json',
			'riscv64.json',
			'rx.json',
			's390.json',
			's390x.json',
			'sh4.json',
			'sparc64.json',
			'sparc.json',
			'vax.json',
			'x86_64.json',
			'xtensa.json',
		],
	},

	entry_points = {
		'console_scripts': [
			'cxc-build = cxc_build:main',
		],
	},

	classifiers = [
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: BSD License',

		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: System Administrators',

		'Topic :: Software Development',
		'Topic :: System :: Hardware',

	],

	project_urls = {
		'Documentation': 'https://github.com/bad-alloc-heavy-industries/cxc-build',
		'Source Code'  : 'https://github.com/bad-alloc-heavy-industries/cxc-build',
		'Bug Tracker'  : 'https://github.com/bad-alloc-heavy-industries/cxc-build/issues',
	}
)
