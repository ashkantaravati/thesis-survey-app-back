from django.db import models
from hashid_field.field import HashidAutoField
from .organization import Organization
from django.contrib.admin import display


class Team(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(
        to=Organization, related_name="teams", on_delete=models.DO_NOTHING
    )

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
        # members = self.members.all()
        if self.queried_members:
            scores_for_member_with_scores = [
                member.average_voice_behavior_score
                for member in self.queried_members
                if member.average_voice_behavior_score
            ]
            if len(scores_for_member_with_scores) > 0:
                return sum(scores_for_member_with_scores) / len(
                    scores_for_member_with_scores
                )
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
