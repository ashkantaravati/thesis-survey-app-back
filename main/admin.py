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

admin.site.register(Organization)
admin.site.register(Team)
# admin.site.register(TeamMemberVoiceEvaluationByParticipant)
# admin.site.register(ParticipantTeamMember)
# admin.site.register(GeneralSurveyResponse)
# admin.site.register(OverconfidenceSurveyResponse)
# admin.site.register(TeamCoordinationSurveyResponse)


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
    verbose_name = "Voice behavior evaluation by teammate about this participant"
    verbose_name_plural = (
        "Voice behavior evaluations by teammates about this participant"
    )


class VoiceEvaluationsByParticipantInline(admin.StackedInline):
    model = TeamMemberVoiceEvaluationByParticipant
    can_delete = False
    fk_name = "evaluating_participant"
    exclude = ("team",)
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
