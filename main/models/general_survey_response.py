from django.db import models
from .participant_team_member import ParticipantTeamMember

SEX_CHOICES = [("male", "آقا"), ("female", "خانم")]


class GeneralSurveyResponse(models.Model):
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10, null=True, blank=True)
    # TODO add tenure and team history
    participant = models.OneToOneField(
        to=ParticipantTeamMember,
        on_delete=models.CASCADE,
        related_name="general_survey_response",
    )

    def __str__(self):
        return f"پرسش‌های عمومی مربوط به {self.participant}  "
