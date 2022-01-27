from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sms/__init__.py
from sms import __version__ as version

setup(
	name="sms",
	version=version,
	description="Custom SMS App",
	author="Salim",
	author_email="dsmwaura@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
