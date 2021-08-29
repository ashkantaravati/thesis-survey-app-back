from django.db import models
from .participant_team_member import ParticipantTeamMember
from .team import Team
from django.contrib.admin import display


class TeamMemberVoiceEvaluationByParticipant(models.Model):
    question_1 = models.IntegerField()
    question_2 = models.IntegerField()
    question_3 = models.IntegerField()
    question_4 = models.IntegerField()
    question_5 = models.IntegerField()
    question_6 = models.IntegerField()
    evaluating_participant = models.ForeignKey(
        to=ParticipantTeamMember,
        on_delete=models.DO_NOTHING,
        related_name="voice_survey_responses",
    )
    evaluated_participant = models.ForeignKey(
        to=ParticipantTeamMember,
        on_delete=models.DO_NOTHING,
        related_name="voice_evaluations_about_participant",
    )
    team = models.ForeignKey(to=Team, on_delete=models.DO_NOTHING)

    @property
    @display(
        description="Voice Behavior Score",
    )
    def score(self):
        if (
            self.question_1
            and self.question_2
            and self.question_3
            and self.question_4
            and self.question_5
            and self.question_6
        ):
            return (
                self.question_1
                + self.question_2
                + self.question_3
                + self.question_4
                + self.question_5
                + self.question_6
            ) / 6

    def __str__(self) -> str:
        return f"نظر {self.evaluating_participant} درباره‌ی رفتار صدای {self.evaluated_participant}"
