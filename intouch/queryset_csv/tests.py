import django
from django.core.management.color import no_style
from django.db import models, connection
from django.db import models
from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from intouch.queryset_csv.shortcuts import queryset_as_csv_response

django.setup()

class QuerysetCsvTests(TestCase):
    
    class TestModel(models.Model):
        '''
        Basic django model for use with this test case
        '''
        class Meta:
            app_label = "queryset_csv.tests"
        
        number = models.IntegerField()
    
    def setUp(self):
        self._style = no_style()
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(self.TestModel)

    
    
    def tearDown(self):
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(self.TestModel)
            
    
    def test_queryset_csv_response(self):
        for i in range(0, 10):
            self.TestModel.objects.create(number=i)
            
        expected = b"""Id,Number\r\n1,0\r\n2,1\r\n3,2\r\n4,3\r\n5,4\r\n6,5\r\n7,6\r\n8,7\r\n9,8\r\n10,9\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.TestModel.objects.all(), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")


        
