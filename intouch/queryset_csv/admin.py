from django.conf import settings
from intouch.queryset_csv.views import queryset_as_csv_response


def export_model_as_csv(admin, request, queryset):
    return queryset_as_csv_response(queryset, is_stream=True)

class CsvExporterAdmin():
    def get_actions(self, *args, **kwargs):
        actions = list(super().get_actions(*args, **kwargs))
        actions.append(export_model_as_csv)
        return actions
