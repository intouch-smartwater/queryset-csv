from intouch.queryset_csv.shortcuts import queryset_as_csv_response


def export_selection_as_csv(admin, request, queryset):
    return queryset_as_csv_response(queryset, is_stream=True)
export_selection_as_csv.short_description='Export Selection as CSV'

class CsvExporterAdmin():
    def get_actions(self, *args, **kwargs):
        actions = list(super().get_actions(*args, **kwargs))
        actions.append(export_selection_as_csv)
        return actions
