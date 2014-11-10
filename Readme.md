# Queryset CSV

Queryset CSV is a simple module to allow Django Querysets to be exported as CSV files.

*Why create this code rather than use an existing CSV export project?*

1. Licensing - Other CSV export packages encountered are Licensed under the GNU GPL. The GPL is incompatible with the desired usage, so a this was written from scratch.
1. Functionality - Existing CSV packages are not designed to handle very large querysets, the option to steam querysets is essential for models with thousands of entries.
1. Simplicity - This package has no dependencies other than django itself, and the requirements are to be kept to a minimum in future versions (preferably solely django). It is also designed to require as little effort as possible to use.
1. Currency - The package is written and tested using the latest versions of Python and Django. While it may work with older versions, no special effort will be expended to force compatibility with old versions.
