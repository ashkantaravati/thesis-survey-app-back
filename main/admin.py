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

    inlines = [
        TeamInline,
    ]


class TeamMemberInline(admin.StackedInline):
    model = ParticipantTeamMember
    can_delete = False


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

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

    inlines = [
        GeneralSurveyResponseInline,
        OverconfidenceSurveyResponseInline,
        TeamCoordinationSurveyResponseInline,
        VoiceEvaluationsAboutParticipantInline,
        VoiceEvaluationsByParticipantInline,
    ]
