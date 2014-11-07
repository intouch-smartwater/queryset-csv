# Queryset CSV

Queryset CSV is a simple module to allow Django Querysets to be exported as CSV files.

*Why create this code rather than use an existing CSV export?*

1. The license, the GPL is incompatible with the desired usage, so a this was written from scratch.
1. Functionality, many existing CSV packages are not designed to handle very large querysets, the option to steam querysets is essential for models with thousands of entries