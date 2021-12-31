from django.db import models
from hashid_field.field import HashidAutoField

from main.typing import ListOfICCFrameRecord
from .organization import Organization
from django.contrib.admin import display
from main.calculations import (
    create_data_frame_for_icc,
    check_interrater_reliability_with_icc,
    get_mean_value_of_list,
)

ERROR_FLAG = "N/A"


class Team(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    size = models.IntegerField(default=3)
    organization = models.ForeignKey(
        to=Organization, related_name="teams", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def coordination_ratings_are_reliable(self):
        df = create_data_frame_for_icc(
            [
                response.team_coordination_as_record()
                for response in self.responses.all()
            ]
        )
        return check_interrater_reliability_with_icc(df)

    def effectiveness_ratings_are_reliable(self):
        df = create_data_frame_for_icc(
            [
                response.team_effectiveness_as_record()
                for response in self.responses.all()
            ]
        )
        return check_interrater_reliability_with_icc(df)

    @property
    def has_participated(self):
        return self.responses.count() > 0

    @property
    @display(
        description="Response Count",
    )
    def number_of_responses(self):
        return self.responses.count()

    @property
    @display(description="Mean Age")
    def mean_age(self):
        ages = [response.age for response in self.responses.all()]
        return get_mean_value_of_list(ages)

    @property
    @display(description="Mean Tenure")
    def mean_tenure(self):
        tenures = [response.tenure for response in self.responses.all()]
        return get_mean_value_of_list(tenures)

    @property
    @display(description="Mean Team History")
    def mean_team_history(self):
        team_histories = [response.team_history for response in self.responses.all()]
        return get_mean_value_of_list(team_histories)

    @property
    @display(
        description="Mean Voice Behavior",
    )
    def mean_voice_behavior(self):
        scores_for_response_with_scores = [
            response.voice_behavior_score for response in self.responses.all()
        ]
        return get_mean_value_of_list(scores_for_response_with_scores)

    @property
    @display(
        description="Team Coordination",
    )
    def mean_team_coordination(self):
        if self.responses and self.coordination_ratings_are_reliable():
            scores = [
                response.team_coordination_score for response in self.responses.all()
            ]
            return get_mean_value_of_list(scores)

        return ERROR_FLAG

    @property
    @display(
        description="Team Effectiveness",
    )
    def mean_team_effectiveness(self):
        if self.responses and self.effectiveness_ratings_are_reliable():
            scores = [
                response.team_effectiveness_score for response in self.responses.all()
            ]
            return get_mean_value_of_list(scores)

        return ERROR_FLAG

    def __str__(self) -> str:
        return f"{self.name} مربوط به {self.organization}"

    @property
    def as_dict(self) -> dict:
        return {
            "team": self.id,
            "org": self.organization.id,
            "team_size": self.size,
            "response_count": self.number_of_responses,
            "mean_age": self.mean_age,
            "mean_tenure": self.mean_tenure,
            "mean_team_history": self.mean_team_history,
            "mean_voice_behavior": self.mean_voice_behavior,
            "mean_team_coordination": self.mean_team_coordination,
            "mean_team_effectiveness": self.mean_team_effectiveness,
        }
