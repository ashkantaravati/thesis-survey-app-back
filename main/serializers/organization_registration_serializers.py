from django.db.models import fields
from rest_framework import serializers
from main.models import (
    Team,
    Organization,
)
from hashid_field.rest import HashidSerializerCharField


class TeamRegistrationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "size"]
        depth = 1


class OrganizationRegistrationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)

    teams = TeamRegistrationSerializer(
        many=True,
    )

    class Meta:
        model = Organization
        fields = ["id", "name", "rep_name", "rep_email", "rep_job_title", "teams"]
        depth = 2

    def create(self, validated_data):
        teams_data = validated_data.pop("teams")
        organization = Organization.objects.create(**validated_data)
        for team_data in teams_data:
            Team.objects.create(organization=organization, **team_data)
        return organization
