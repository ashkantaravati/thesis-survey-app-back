from django.db.models import fields
from rest_framework import serializers
from .models import (
    GeneralSurveyResponse,
    OverconfidenceSurveyResponse,
    ParticipantTeamMember,
    Team,
    Organization,
    TeamCoordinationSurveyResponse,
    TeamMemberVoiceEvaluationByParticipant,
)
from hashid_field.rest import HashidSerializerCharField

SURVEY_LINK_BASE_URL = "http://localhost:8080/participate/"
# TODO retire generation of link in backend


class ParticipantTeamMemberSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField()

    class Meta:
        model = ParticipantTeamMember
        fields = ["id", "name"]


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


class InitialTeamMemberRegistrationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)

    class Meta:
        model = ParticipantTeamMember
        fields = ["id", "name"]


class TeamRegistrationSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)
    link = serializers.SerializerMethodField("get_survey_link", read_only=True)

    def get_survey_link(self, obj):
        return SURVEY_LINK_BASE_URL + str(obj.id)

    members = InitialTeamMemberRegistrationSerializer(
        many=True,
    )

    class Meta:
        model = Team
        fields = ["id", "name", "members", "link"]
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


class VoiceEvaluationSerializer(serializers.ModelSerializer):
    evaluated_participant = ParticipantTeamMemberSerializer()
    # id = HashidSerializerCharField(read_only=True)

    class Meta:
        model = TeamMemberVoiceEvaluationByParticipant
        exclude = ["team", "evaluating_participant"]


class GeneralSurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSurveyResponse
        exclude = ["participant"]


class TeamCoordinationSurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCoordinationSurveyResponse
        exclude = ["participant"]


class OverconfidenceSurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverconfidenceSurveyResponse
        exclude = ["participant"]


class TeamMemberParticipationSerializer(serializers.ModelSerializer):
    voice_survey_responses = VoiceEvaluationSerializer(many=True)
    general_survey_response = GeneralSurveyResponseSerializer()
    overconfidence_survey_response = OverconfidenceSurveyResponseSerializer()
    team_coordination_survey_response = TeamCoordinationSurveyResponseSerializer()

    id = HashidSerializerCharField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = ParticipantTeamMember
        exclude = ["organization", "team", "has_participated"]
        depth = 2

    def update(self, instance, validated_data):
        if instance.has_participated:
            raise serializers.ValidationError("Already participated")
        voice_survey_responses = validated_data.get("voice_survey_responses")
        for voice_survey_response in voice_survey_responses:
            evaluated_participant_data = voice_survey_response.pop(
                "evaluated_participant"
            )
            evaluated_participant = ParticipantTeamMember.objects.get(
                pk=evaluated_participant_data.get("id")
            )
            TeamMemberVoiceEvaluationByParticipant.objects.create(
                evaluating_participant=instance,
                team=instance.team,
                evaluated_participant=evaluated_participant,
                **voice_survey_response
            )
        GeneralSurveyResponse.objects.create(
            participant=instance, **validated_data.get("general_survey_response")
        )
        OverconfidenceSurveyResponse.objects.create(
            participant=instance, **validated_data.get("overconfidence_survey_response")
        )
        TeamCoordinationSurveyResponse.objects.create(
            participant=instance,
            **validated_data.get("team_coordination_survey_response")
        )
        instance.has_participated = True
        instance.save()
        return instance
