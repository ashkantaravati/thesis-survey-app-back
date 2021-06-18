from django.contrib import admin
from .models import (
    Organization,
    Team,
    ParticipantTeamMember,
    TeamMemberVoiceEvaluationByParticipant,
)

admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(TeamMemberVoiceEvaluationByParticipant)
admin.site.register(ParticipantTeamMember)
