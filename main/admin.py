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
admin.site.register(TeamMemberVoiceEvaluationByParticipant)
admin.site.register(ParticipantTeamMember)
admin.site.register(GeneralSurveyResponse)
admin.site.register(OverconfidenceSurveyResponse)
admin.site.register(TeamCoordinationSurveyResponse)
