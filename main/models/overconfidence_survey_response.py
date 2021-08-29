from django.db import models
from .participant_team_member import ParticipantTeamMember


class OverconfidenceSurveyResponse(models.Model):
    question_1_min = models.IntegerField(null=True, blank=True)
    question_1_max = models.IntegerField(null=True, blank=True)
    question_2_min = models.IntegerField(null=True, blank=True)
    question_2_max = models.IntegerField(null=True, blank=True)
    question_3_min = models.IntegerField(null=True, blank=True)
    question_3_max = models.IntegerField(null=True, blank=True)
    question_4_min = models.IntegerField(null=True, blank=True)
    question_4_max = models.IntegerField(null=True, blank=True)
    question_5_min = models.IntegerField(null=True, blank=True)
    question_5_max = models.IntegerField(null=True, blank=True)
    question_6_min = models.IntegerField(null=True, blank=True)
    question_6_max = models.IntegerField(null=True, blank=True)
    question_7_min = models.IntegerField(null=True, blank=True)
    question_7_max = models.IntegerField(null=True, blank=True)
    question_8_min = models.IntegerField(null=True, blank=True)
    question_8_max = models.IntegerField(null=True, blank=True)
    question_9_min = models.IntegerField(null=True, blank=True)
    question_9_max = models.IntegerField(null=True, blank=True)
    question_10_min = models.IntegerField(null=True, blank=True)
    question_10_max = models.IntegerField(null=True, blank=True)
    participant = models.OneToOneField(
        to=ParticipantTeamMember,
        on_delete=models.CASCADE,
        related_name="overconfidence_survey_response",
    )

    @property
    def score(self):
        pass
