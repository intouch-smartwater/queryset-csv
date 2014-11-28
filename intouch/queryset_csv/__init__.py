default_app_config = 'intouch.queryset_csv.apps.QuerysetCSVAppConfig'

from .views import queryset_as_csv_response
from .admin import export_model_as_csv, CsvExporterAdmin