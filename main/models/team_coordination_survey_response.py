from django.db import models
from main.calculations import round_as_default

from main.typing import ICCFrameRecord
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

    def as_record(self) -> ICCFrameRecord:
        return (self.participant.id.hashid, self.participant.team.id.hashid, self.score)

    @property
    def score(self):
        raw_score = (
            self.question_1
            + self.question_2
            + self.question_3
            + self.question_4
            + self.question_5
        ) / 5
        rounded_score = round_as_default(raw_score)
        return rounded_score
