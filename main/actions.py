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


def export_as_csv(modeladmin, request, queryset):
    # check if queryset is from a model with a property 'as_dict'
    # if so, serialize the queryset as csv
    # otherwise, respond with a 404
    if hasattr(queryset.model, "as_dict"):
        data = [record.as_dict for record in queryset]
        response = HttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": f'attachment; filename="{modeladmin.model_plural_name}.csv"'
            },
        )
        writer = csv.DictWriter(response, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        return response
    return HttpResponse(status=404)
