from django.db import models
from .participant_team_member import ParticipantTeamMember


class Feedback(models.Model):
    response = models.TextField(null=True, blank=True)
    participant = models.OneToOneField(
        to=ParticipantTeamMember,
        on_delete=models.CASCADE,
        related_name="feedback",
    )

    def __str__(self):
        return f"{self.participant}:{self.response}"
