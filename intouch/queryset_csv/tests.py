import django
from django.core.management.color import no_style
from django.db import models, connection
from django.test import TestCase
from django.test.client import Client

django.setup()

class QuerysetCsvTests(TestCase):
    
    class TestModel(models.Model):
        '''
        Basic django model for use with this test case
        '''
    
    def setUp(self):
        self._style = no_style()
        sql, _ = connection.creation.sql_create_model(self.TestModel, self._style)
        self._cursor = connection.cursor()
        for statement in sql:
            self._cursor.execute(statement)
    
    
    def tearDown(self):
        sql = connection.creation.sql_destroy_model(self.TestModel, (), self._style)
        for statement in sql:
            self._cursor.execute(statement)
            
    
    def test_queryset_csv_response(self):
        for _ in range(0, 10):
            self.TestModel.objects.create()
        client = Client()
        