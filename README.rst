============
Queryset CSV
============

Queryset CSV is a simple module to allow Django Querysets to be exported as CSV files.

------------
Installation
------------
::

	pip install intouch-queryset-csv
	
Then add the app to your installed apps ::

	intouch.queryset_csv
	
-----
Usage
-----

There are several ways to use the Queryset csv exporter.

^^^^^^^^^^^^^^^^^^
Render to response
^^^^^^^^^^^^^^^^^^

The most basic usage is to call the function ::

	queryset_as_csv_response
	
This function accepts a queryset as a parameter, along with a filename and whether the file is to be streamed.
It returns an HTTPResponse object, so should be called at the end of a view function to offer the download
to the client.

^^^^^^^^^^^^
Admin Action
^^^^^^^^^^^^

An action is provided for the Django admin site. There are 3 ways of including it:

#. The function :code:`export_model_as_csv` can be added to your custom admin class's actions
#. The :code:`CsvExporterAdmin` class can be inherited to provide the action
#. Setting :code:`CSV_EXPORT_ADMIN_ACTION_AVAILABLE=True` in your django settings module will make the action available to all registered admin classes.
	
The action will simply export all objects of the selected model to csv (as a stream)  

--------------------------------------------------------------------
Why create this code rather than use an existing CSV export project?
--------------------------------------------------------------------

#. Licensing - Other CSV export packages encountered are Licensed under the GNU GPL. The GPL is incompatible with the desired usage, so a this was written from scratch.
#. Functionality - Existing CSV packages are not designed to handle very large querysets, the option to steam querysets is essential for models with thousands of entries.
#. Simplicity - This package has no dependencies other than django itself, and the requirements are to be kept to a minimum in future versions (preferably solely django). It is also designed to require as little effort as possible to use.
#. Currency - The package is written and tested using the latest versions of Python and Django. While it may work with older versions, no special effort will be expended to force compatibility with old versions.

---------------
Tested Versions
---------------

Django versions 1.7-1.10 should be supported, Python 3 versions supported as per the Django releases.
