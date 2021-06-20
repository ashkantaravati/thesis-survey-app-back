from rest_framework import serializers
from .models import ParticipantTeamMember, Team, Organization
from hashid_field.rest import HashidSerializerCharField


class ParticipantTeamMemberSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    class Meta:
        model = ParticipantTeamMember
        fields = ["id", "name"]


class OrganizationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    class Meta:
        model = Organization
        fields = ["id", "name"]


class TeamSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    members = ParticipantTeamMemberSerializer(
        many=True,
        read_only=True,
        source="participantteammember_set",
    )

    organization = OrganizationSerializer(
        read_only=True,
    )

    class Meta:
        model = Team
        fields = ["id", "name", "members", "organization"]
        depth = 1
