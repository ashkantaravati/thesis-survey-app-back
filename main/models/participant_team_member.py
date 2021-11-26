from django.db import models
from hashid_field.field import HashidAutoField

from main.typing import ICCFrameRecord, ListOfICCFrameRecord
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
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def voice_ratings_as_records(self) -> ListOfICCFrameRecord:
        all_evaluations = self.voice_evaluations_about_participant.all()
        list_of_records = [evaluation.as_record() for evaluation in all_evaluations]
        return list_of_records

    def coordination_ratings_as_record(self) -> ICCFrameRecord:
        record = self.team_coordination_survey_response.as_record()
        return record

    def effectiveness_ratings_as_record(self) -> ICCFrameRecord:
        try:
            return self.team_effectiveness_survey_response.as_record()
        except:
            return (self.id.hashid, self.team.id.hashid, 0)

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

    @property
    @display(
        description="age",
    )
    def age(self) -> int:
        return self.general_survey_response.age

    @property
    @display(
        description="tenure",
    )
    def tenure(self) -> int:
        return self.general_survey_response.tenure

    @property
    @display(
        description="team_history",
    )
    def team_history(self) -> int:
        return self.general_survey_response.team_history

    @property
    @display(
        description="sex",
    )
    def sex(self):
        return self.general_survey_response.sex

    @property
    @display(
        description="Opinion on Team Coordination Score",
    )
    def opinion_on_team_coordination_score(self):
        return self.team_coordination_survey_response.score

    @property
    @display(
        description="Opinion on Team Effectiveness Score",
    )
    def opinion_on_team_effectiveness_score(self):
        return self.team_effectiveness_survey_response.score
