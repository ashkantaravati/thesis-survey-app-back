from django.db import models
from hashid_field.field import HashidAutoField
from .organization import Organization
from .team import Team
from django.contrib.admin import display


class ParticipantTeamMember(models.Model):
    id = HashidAutoField(primary_key=True)
    has_participated = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    team = models.ForeignKey(
        to=Team, related_name="members", on_delete=models.DO_NOTHING
    )
    organization = models.ForeignKey(to=Organization, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    @display(
        description="Average Voice Behavior Score by Teammate evaluations",
    )
    def average_voice_behavior_score(self) -> float:
        evaluations = self.voice_evaluations_about_participant.all()
        if evaluations:
            submitted_scores = [
                evaluation.score for evaluation in evaluations if evaluation.score
            ]
            return sum(submitted_scores) / len(submitted_scores)
