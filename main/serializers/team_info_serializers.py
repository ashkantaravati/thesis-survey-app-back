from django.db.models import fields
from rest_framework import serializers
from main.models import (
    ParticipantTeamMember,
    Team,
    Organization,
)
from hashid_field.rest import HashidSerializerCharField


class NotParticipatedListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(has_participated=False)
        return super(NotParticipatedListSerializer, self).to_representation(data)


class NonParticipatedTeamMemberSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    class Meta:
        list_serializer_class = NotParticipatedListSerializer
        model = ParticipantTeamMember
        fields = ["id", "name"]


class OrganizationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    class Meta:
        model = Organization
        fields = ["id", "name"]


class TeamSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    members = NonParticipatedTeamMemberSerializer(
        many=True,
        read_only=True,
    )

    organization = OrganizationSerializer(
        read_only=True,
    )

    class Meta:
        model = Team
        fields = ["id", "name", "members", "organization"]
        depth = 1
