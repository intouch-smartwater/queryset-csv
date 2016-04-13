from django.apps.registry import apps
from django.views.generic.base import View
from intouch.queryset_csv.shortcuts import queryset_as_csv_response
from django.core.exceptions import PermissionDenied


class ModelAsCsvView(View):
    
    def get(self, request, app, model):
        
        Model = apps.get_model(app, model)
        
        if self.has_export_permission(request.user, Model):
            return queryset_as_csv_response(Model.objects.all(), is_stream=True)
        else :
            raise PermissionDenied
        
        
    def has_export_permission(self, user, Model):
        return True # TODO check for permission
