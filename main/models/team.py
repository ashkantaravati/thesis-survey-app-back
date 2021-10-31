from django.db import models
from hashid_field.field import HashidAutoField
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

    def voice_ratings_as_records(self):
        records = []
        for member in self.members.all():
            records += member.voice_ratings_as_records()
        return records

    def voice_ratings_are_reliable(self):
        df = create_data_frame_for_icc(self.voice_ratings_as_records())
        return check_interrater_reliability_with_icc(df)

    @property
    def queried_members(self) -> list:
        return self.members.filter(has_participated=True)

    @property
    @display(
        description="Number of Members",
    )
    def number_of_members(self):
        return self.members.count()

    @property
    @display(
        description="Number of Participated Members",
    )
    def number_of_participated_members(self):
        return self.queried_members.count()

    @property
    @display(description="Average Team Member Age")
    def average_member_age(self):
        # participated_members = self.members.filter(has_participated=True)
        ages = [member.age for member in self.queried_members]
        return sum(ages) / len(ages) if ages else 0

    @property
    @display(description="Average Team Member Tenure")
    def average_member_tenure(self):
        # participated_members = self.members.filter(has_participated=True)
        tenures = [member.tenure for member in self.queried_members]
        return sum(tenures) / len(tenures) if tenures else 0

    @property
    @display(description="Average Team Member Team History")
    def average_member_team_history(self):
        # participated_members = self.members.filter(has_participated=True)
        team_histories = [member.team_history for member in self.queried_members]
        return sum(team_histories) / len(team_histories) if team_histories else 0

    @property
    @display(
        description="Average Team Member Voice Behavior",
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
        description="Average Opinion on Team Coordination",
    )
    def average_team_coordination(self):
        scores = [
            member.opinion_on_team_coordination_score
            for member in self.queried_members
            if member.opinion_on_team_coordination_score
        ]
        return sum(scores) / len(scores) if scores else 0

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
