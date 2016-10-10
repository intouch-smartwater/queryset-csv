'''
Created on 1 Dec 2014

@author: james.mcmahon
'''

from django.conf.urls import url
from intouch.queryset_csv.views import ModelAsCsvView

urlpatterns = [
    url(r'(?P<app>[0-9A-Za-z_]+)/(?P<model>[0-9A-Za-z_]+)/', ModelAsCsvView.as_view())
]
