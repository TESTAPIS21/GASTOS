from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in f_gastos/__init__.py
from f_gastos import __version__ as version

setup(
	name="f_gastos",
	version=version,
	description="Gastos",
	author="sistemas",
	author_email="aguimashoes362@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
