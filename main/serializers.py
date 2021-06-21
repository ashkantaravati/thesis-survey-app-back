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
    )

    organization = OrganizationSerializer(
        read_only=True,
    )

    class Meta:
        model = Team
        fields = ["id", "name", "members", "organization"]
        depth = 1


class InitialTeamMemberRegistrationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)

    class Meta:
        model = ParticipantTeamMember
        fields = ["id", "name"]


class TeamRegistrationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)

    members = InitialTeamMemberRegistrationSerializer(
        many=True,
    )

    class Meta:
        model = Team
        fields = ["id", "name", "members"]
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
            members_data = team_data.pop("members")
            team = Team.objects.create(organization=organization, **team_data)
            for member_data in members_data:
                ParticipantTeamMember.objects.create(
                    team=team, organization=organization, **member_data
                )

        return organization


class TeamMemberParticipationSerializer(serializers.ModelSerializer):
    pass
