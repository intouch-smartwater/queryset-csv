'''
Created on 28 Nov 2014

@author: james.mcmahon
'''
from django.apps.config import AppConfig
from django.conf import settings
from django.contrib import admin
from intouch.queryset_csv.admin import export_selection_as_csv


class QuerysetCSVAppConfig(AppConfig):
    name = 'intouch.queryset_csv'
    verbose_name = 'Queryset CSV'
    
    def ready(self):
        if getattr(settings, 'CSV_EXPORT_ADMIN_ACTION_AVAILABLE', False):
            admin.site.add_action(export_selection_as_csv)
