from django.db.models import fields
from rest_framework import serializers
from main.models import (
    Team,
    Organization,
)
from hashid_field.rest import HashidSerializerCharField


class OrganizationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    class Meta:
        model = Organization
        fields = ["id", "name"]


class TeamSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    organization = OrganizationSerializer(
        read_only=True,
    )

    class Meta:
        model = Team
        fields = ["id", "name", "organization"]
        depth = 1
