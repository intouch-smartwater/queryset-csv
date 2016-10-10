from setuptools import setup

setup(
	name='intouch_queryset_csv',
	version='0.1.3',
	description='Module to export django querysets as csv files',
	maintainer='James Cheese',
	maintainer_email='james.cheese@intouch-ltd.com',
	url='https://bitbucket.org/intouchltd/queryset-csv',
	packages=['intouch', 'intouch.queryset_csv'],
	keywords='django queryset csv',
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Environment :: Plugins',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.2',
		
	],
	install_requires=['django>=1.7']
)
