import datetime
import django
from django.core.management.color import no_style
from django.db import models, connection
from django.db import models
from django.test import TransactionTestCase
from django.test.client import Client
from django.conf import settings
from intouch.queryset_csv.shortcuts import queryset_as_csv_response

django.setup()

class QuerysetCsvTests(TransactionTestCase):
    
    class IntegerTestModel(models.Model):
        '''
        Basic django model for use with this test case
        '''
        class Meta:
            app_label = "queryset_csv.tests"
        
        number = models.IntegerField()
    
    class ComplexTestModel(models.Model):
        '''
        Basic django model for use with this test case
        '''
        class Meta:
            app_label = "queryset_csv.tests"
        
        integer = models.IntegerField()
        char = models.CharField(max_length=32)
        datetime = models.DateTimeField()
    
    def setUp(self):
        self._style = no_style()
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(self.IntegerTestModel)
            schema_editor.create_model(self.ComplexTestModel)

    
    
    def tearDown(self):
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(self.IntegerTestModel)
            schema_editor.delete_model(self.ComplexTestModel)

    
    def test_queryset_csv_response(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id,Number\r\n1,0\r\n2,1\r\n3,2\r\n4,3\r\n5,4\r\n6,5\r\n7,6\r\n8,7\r\n9,8\r\n10,9\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all(), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")


    def test_queryset_csv_response_values_one_field(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().values('id'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")

    def test_queryset_csv_response_values_two_fields(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id,Number\r\n1,0\r\n2,1\r\n3,2\r\n4,3\r\n5,4\r\n6,5\r\n7,6\r\n8,7\r\n9,8\r\n10,9\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().values('id', 'number'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")

    def test_queryset_csv_response_values_ordering(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Number,Id\r\n0,1\r\n1,2\r\n2,3\r\n3,4\r\n4,5\r\n5,6\r\n6,7\r\n7,8\r\n8,9\r\n9,10\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().values('number', 'id'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")
        

    def test_queryset_csv_response_values_list_one_field(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().values_list('id'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")

    def test_queryset_csv_response_values_list_two_fields(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id,Number\r\n1,0\r\n2,1\r\n3,2\r\n4,3\r\n5,4\r\n6,5\r\n7,6\r\n8,7\r\n9,8\r\n10,9\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().values_list('id', 'number'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")

    def test_queryset_csv_response_values_list_ordering(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Number,Id\r\n0,1\r\n1,2\r\n2,3\r\n3,4\r\n4,5\r\n5,6\r\n6,7\r\n7,8\r\n8,9\r\n9,10\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().values_list('number', 'id'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")


    def test_queryset_csv_response_values_one_field_with_only(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().only('number').values('id'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")

    def test_queryset_csv_response_values_two_fields_with_only(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id,Number\r\n1,0\r\n2,1\r\n3,2\r\n4,3\r\n5,4\r\n6,5\r\n7,6\r\n8,7\r\n9,8\r\n10,9\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().only('number').values('id', 'number'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")

    def test_queryset_csv_response_values_ordering_with_only(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Number,Id\r\n0,1\r\n1,2\r\n2,3\r\n3,4\r\n4,5\r\n5,6\r\n6,7\r\n7,8\r\n8,9\r\n9,10\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().only('number').values('number', 'id'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")
        

    def test_queryset_csv_response_values_one_field_with_defer(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n"""
        expected_filename = "some_file.csv"
        

        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().defer('id', 'number').values('id'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")

    def test_queryset_csv_response_values_two_fields_with_defer(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Id,Number\r\n1,0\r\n2,1\r\n3,2\r\n4,3\r\n5,4\r\n6,5\r\n7,6\r\n8,7\r\n9,8\r\n10,9\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().defer('number').values('id', 'number'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")

    def test_queryset_csv_response_values_ordering_with_defer(self):
        for i in range(0, 10):
            self.IntegerTestModel.objects.create(number=i)
            
        expected = b"""Number,Id\r\n0,1\r\n1,2\r\n2,3\r\n3,4\r\n4,5\r\n5,6\r\n6,7\r\n7,8\r\n8,9\r\n9,10\r\n"""
        expected_filename = "some_file.csv"
        
        response = queryset_as_csv_response(self.IntegerTestModel.objects.all().defer('number').values('number', 'id'), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")
 

    def test_queryset_csv_response_complex_values(self):
        for i in range(0, 2):
            self.ComplexTestModel.objects.create(integer=i, char='abc\nde,./[];#"\'',datetime=datetime.datetime(2000,1,2))

        expected = b'''Id,Integer,Char,Datetime\r\n1,0,"abc\nde,./[];#""\'",02-01-2000 00:00:00\r\n2,1,"abc\nde,./[];#""\'",02-01-2000 00:00:00\r\n'''
        expected_filename = "other_file.csv"
        
        response = queryset_as_csv_response(self.ComplexTestModel.objects.all(), expected_filename)
        self.assertEqual(expected, response.content, "Comparing response body (as bytes)")
        self.assertEqual("text/csv", response["Content-Type"], "Ensure content type is csv")
        self.assertEqual("attachment; filename={}".format(expected_filename), response["content-disposition"], "Ensuring filename is correctly propogated")
       
