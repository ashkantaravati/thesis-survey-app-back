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


class Team(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(
        to=Organization, related_name="teams", on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def has_participated(self) -> bool:
        return self.number_of_participated_members > 0

    def voice_ratings_as_records(self) -> ListOfICCFrameRecord:
        records = []
        for member in self.members.all():
            records += member.voice_ratings_as_records()
        return records

    def coordination_ratings_as_records(self) -> ListOfICCFrameRecord:
        records = []
        for member in self.members.all():
            records.append(member.coordination_ratings_as_record())
        return records

    def effectiveness_ratings_as_records(self) -> ListOfICCFrameRecord:
        records = []
        for member in self.members.all():
            records.append(member.effectiveness_ratings_as_record())
        return records

    def voice_ratings_are_reliable(self):
        df = create_data_frame_for_icc(self.voice_ratings_as_records())
        return check_interrater_reliability_with_icc(df)

    def coordination_ratings_are_reliable(self):
        df = create_data_frame_for_icc(self.coordination_ratings_as_records())
        return check_interrater_reliability_with_icc(df)

    def effectiveness_ratings_are_reliable(self):
        df = create_data_frame_for_icc(self.effectiveness_ratings_as_records())
        return check_interrater_reliability_with_icc(df)

    @property
    def queried_members(self) -> list:
        return self.members.filter(has_participated=True)

    @property
    @display(
        description="Size",
    )
    def number_of_members(self):
        return self.members.count()

    @property
    @display(
        description="No. of Participated",
    )
    def number_of_participated_members(self):
        return self.queried_members.count()

    @property
    @display(description="Average Age")
    def average_member_age(self):
        ages = [member.age for member in self.queried_members]
        return get_mean_value_of_list(ages)

    @property
    @display(description="Average Tenure")
    def average_member_tenure(self):
        tenures = [member.tenure for member in self.queried_members]
        return get_mean_value_of_list(tenures)

    @property
    @display(description="Average Team History")
    def average_member_team_history(self):
        team_histories = [member.team_history for member in self.queried_members]
        return get_mean_value_of_list(team_histories)

    @property
    @display(
        description="Voice Behavior",
    )
    def average_voice_behavior(self):
        if self.queried_members and self.voice_ratings_are_reliable():
            scores_for_member_with_scores = [
                member.average_voice_behavior_score
                for member in self.queried_members
                if member.average_voice_behavior_score
            ]
            mean = get_mean_value_of_list(scores_for_member_with_scores)
            if mean:
                return mean
        return "N/A"

    @property
    @display(
        description="Team Coordination",
    )
    def average_team_coordination(self):
        if self.queried_members and self.coordination_ratings_are_reliable():
            scores = [
                member.opinion_on_team_coordination_score
                for member in self.queried_members
                if member.opinion_on_team_coordination_score
            ]
            return get_mean_value_of_list(scores)

        return "N/A"

    def __str__(self) -> str:
        return f"{self.name} مربوط به {self.organization}"

    @property
    def as_dict(self) -> dict:
        return {
            "team": self.id,
            "org": self.organization.id,
            "team_size": self.number_of_participated_members,
            "average_member_age": self.average_member_age,
            "average_member_tenure": self.average_member_tenure,
            "average_member_team_history": self.average_member_team_history,
            "average_voice_behavior": self.average_voice_behavior,
            "average_team_coordination": self.average_team_coordination,
        }
