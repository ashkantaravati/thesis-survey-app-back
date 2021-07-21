from django.db import models
from .participant_team_member import ParticipantTeamMember


class TeamCoordinationSurveyResponse(models.Model):
    question_1 = models.IntegerField(null=True, blank=True)
    question_2 = models.IntegerField(null=True, blank=True)
    question_3 = models.IntegerField(null=True, blank=True)
    question_4 = models.IntegerField(null=True, blank=True)
    question_5 = models.IntegerField(null=True, blank=True)
    participant = models.OneToOneField(
        to=ParticipantTeamMember,
        on_delete=models.CASCADE,
        related_name="team_coordination_survey_response",
    )
