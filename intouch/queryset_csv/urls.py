'''
Created on 1 Dec 2014

@author: james.mcmahon
'''

from django.conf.urls import patterns, url
from intouch.queryset_csv.views import ModelAsCsvView

urlpatterns = patterns('',
    url(r'(?P<app>[0-9A-Za-z_]+)/(?P<model>[0-9A-Za-z_]+)/', ModelAsCsvView.as_view())
)
