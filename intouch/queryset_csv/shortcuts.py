import csv

from django.db.models.query import QuerySet
from django.http.response import HttpResponse, StreamingHttpResponse


def csv_write_to_file(file, headers, data):
    '''
    Write a csv to a given file-like stream target. Returns the original stream.    
    If given a file name, it will automatically open a file stream with mode in replace mode.
    User of this function must close the returned file handler manually or use with a "with" statement.
    '''
    if isinstance(file, str):
        file = open(file, 'w', newline='')

    writer = csv.writer(file, csv.excel)

    if headers:
        writer.writerow(headers)

    for row in data:
        writer.writerow(row)

    return file

def csv_response(filename, headers, data):
    '''
    Create and return a csv as specified in the parameters
    '''
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    
    # response is a file-like object, and can be used as such.
    return csv_write_to_file(response, headers, data)
    

def csv_stream(filename, headers, data):
    '''
    Stream the given data to the client as a csv
    This is useful when data is generated and therefore not
    loaded all at once (e.g. when streaming a very large dataset)
    if data is all loaded (e.g. a python list) this function has
    no benefit over the none-streaming response
    '''
    class Echo:
        '''
        Object to implement the file-like API method
        #write to simply return the given value, as
        StreamingHttpResponse cannot use file-like objects
        '''
        def write(self, value):
            return value
    
    def stream(headers, data):
        '''
        Generator to yeild first the headers then each data row
        data may also be generated, allowing the stream to take up little memory
        '''
        if headers:
            yield headers
        for row in data:
            yield row
        
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer, csv.excel)
    response = StreamingHttpResponse(
        (writer.writerow(row) for row in stream(headers, data)),
        content_type='text/csv'
    )
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename
    return response

def queryset_as_csv_response(queryset, filename=None, is_stream=False):
    '''
    Converts the given queryset to a csv and returns an HttpResponse
    '''
    # Extract the names must using values() to create the correct type of
    # object.
    v_queryset = None
    if isinstance(queryset, QuerySet):
        v_queryset = queryset.values()
    else:
        raise TypeError('queryset must be a django Queryset')
    
    model = v_queryset.model
    try:
        field_names = v_queryset.query.values_select
    except AttributeError:
        field_names = v_queryset.field_names

    
    # Use the model reference to get the verbose names of fields
    verbose_names = []
    for field in field_names:
        verbose_names.append(model._meta.get_field(field).verbose_name.title())
    
    # use the model name if no filename is given
    if filename is None:
        filename = "%s.csv" % model._meta.model_name.title()
        
    
    def data():
        for obj in v_queryset:
            yield [obj[field] for field in field_names] #yield one row of the queryset at a time
    
    if not is_stream:
        return csv_response(filename, verbose_names, data())
    else:
        return csv_stream(filename, verbose_names, data())

