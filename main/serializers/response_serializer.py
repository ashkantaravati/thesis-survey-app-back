from django.db.models import fields
from rest_framework import serializers
from main.models import (
    Response,
)
from hashid_field.rest import HashidSerializerCharField

from main.serializers.team_info_serializers import TeamSerializer


class ResponseSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)
    team = TeamSerializer()

    class Meta:
        model = Response
        fields = "__all__"
        depth = 1
