from django.core import serializers
from django.http import HttpResponse
import csv


def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize(
        "json",
        queryset,
        stream=response,
    ),
    return response


def export_dataset_as_csv_with_autocutoff(modeladmin, request, queryset):
    return export_as_csv(modeladmin, request, queryset, auto_cutoff=True)


def export_as_csv(modeladmin, request, queryset, auto_cutoff=False):
    # check if queryset is from a model with a property 'as_dict'
    # if so, serialize the queryset as csv
    # otherwise, respond with a 404
    if hasattr(queryset.model, "as_dict"):
        if auto_cutoff:
            data = [record.as_dict for record in queryset if record.is_useful]
        else:
            data = [record.as_dict for record in queryset]
        response = HttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": f'attachment; filename="{modeladmin.export_file_name}.csv"'
            },
        )
        writer = csv.DictWriter(response, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        return response
    return HttpResponse(status=404)
