from setuptools import setup

# Load README
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name='intouch_queryset_csv',
	version='0.3.1',
	description='Module to export django querysets as csv files',
	maintainer='James Cheese',
	maintainer_email='james.cheese@intouch-ltd.com',
	url='https://github.com/intouch-smartwater/queryset-csv',
	packages=['intouch', 'intouch.queryset_csv'],
	keywords='django queryset csv',
    long_description=long_description,
    long_description_content_type='text/x-rst',
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Environment :: Plugins',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
	install_requires=['django>=1.7']
)
