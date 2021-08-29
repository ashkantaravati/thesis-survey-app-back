from django.contrib import admin
from .models import (
    Organization,
    Team,
    ParticipantTeamMember,
    TeamMemberVoiceEvaluationByParticipant,
    GeneralSurveyResponse,
    OverconfidenceSurveyResponse,
    TeamCoordinationSurveyResponse,
)


class TeamInline(admin.StackedInline):
    model = Team
    can_delete = False


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rep_name", "number_of_teams")

    inlines = [
        TeamInline,
    ]


class TeamMemberInline(admin.StackedInline):
    model = ParticipantTeamMember
    can_delete = False


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "organization",
        "number_of_members",
        "number_of_participated_members",
        "average_member_age",
        "average_member_tenure",
        "average_member_team_history",
        "average_voice_behavior",
        "average_team_coordination",
    )

    inlines = [
        TeamMemberInline,
    ]


class GeneralSurveyResponseInline(admin.StackedInline):
    model = GeneralSurveyResponse


class OverconfidenceSurveyResponseInline(admin.StackedInline):
    model = OverconfidenceSurveyResponse
    can_delete = False


class TeamCoordinationSurveyResponseInline(admin.StackedInline):
    model = TeamCoordinationSurveyResponse
    can_delete = False


class VoiceEvaluationsAboutParticipantInline(admin.StackedInline):
    model = TeamMemberVoiceEvaluationByParticipant
    can_delete = False
    fk_name = "evaluated_participant"
    exclude = ("team",)
    readonly_fields = ("score",)
    verbose_name = "Voice behavior evaluation by teammate about this participant"
    verbose_name_plural = (
        "Voice behavior evaluations by teammates about this participant"
    )


class VoiceEvaluationsByParticipantInline(admin.StackedInline):
    model = TeamMemberVoiceEvaluationByParticipant
    can_delete = False
    fk_name = "evaluating_participant"
    exclude = ("team",)
    readonly_fields = ("score",)
    verbose_name = "Voice behavior evaluation by this participant about teammate"
    verbose_name_plural = (
        "Voice behavior evaluations by this participant about teammates"
    )


@admin.register(ParticipantTeamMember)
class ParticipantTeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "team",
        "organization",
        "average_voice_behavior_score",
    )

    readonly_fields = ["average_voice_behavior_score"]

    inlines = [
        GeneralSurveyResponseInline,
        OverconfidenceSurveyResponseInline,
        TeamCoordinationSurveyResponseInline,
        VoiceEvaluationsAboutParticipantInline,
        VoiceEvaluationsByParticipantInline,
    ]
