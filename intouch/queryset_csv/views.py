import csv

from django.http.response import HttpResponse
from django.db.models.query import ValuesQuerySet, QuerySet


def queryset_as_csv_response(queryset, filename=None):
	'''
	Converts the given queryset to a csv and returns an HttpResponse
	'''
	# Querysets do not have a reference to the field names list,
	# however, ValuesQuerySets do. If this is not a valuesQuerySet
	# the names must be extracted by using values() to create
	# the correct type of object to get the names
	
	v_queryset = None
	if isinstance(queryset, ValuesQuerySet):
		v_queryset = queryset
	elif isinstance(queryset, QuerySet):
		v_queryset = queryset.values()
	else:
		raise TypeError('queryset must be a django Queryset')
	
	model = v_queryset.model
	field_names = v_queryset.field_names

	
	# Use the model reference to get the verbose names of fields
	verbose_names = []
	for field in field_names:
		verbose_names.append(model._meta.get_field(field).verbose_name.title())
	
	# use the model name if no filename is given
	if filename is None:
		filename = "%s.csv" % model._meta.model_name.title()
		
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	writer = csv.writer(response, csv.excel)
	response.write('\ufeff'.encode('utf8')) # BOM (Excel needs this to open UTF-8 file properly)

	writer.writerow(verbose_names)
	
	for obj in v_queryset: 
		row = []
		for field in field_names:
			row.append(obj[field]) #ValuesQueryset returns dicts, not objects
		writer.writerow(row)
	return response