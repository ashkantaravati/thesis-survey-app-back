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

    @display(
        description="Number of Members",
    )
    def number_of_members(self):
        return self.members.count()

    @display(
        description="Number of Participated Members",
    )
    def number_of_participated_members(self):
        return self.members.filter(has_participated=True).count()

    @display(
        description="Average Team Member Voice Behavior",
    )
    def average_voice_behavior(self):
        members = self.members.all()
        if members:
            scores_for_member_with_scores = [
                member.average_voice_behavior_score
                for member in members
                if member.average_voice_behavior_score
            ]
            if len(scores_for_member_with_scores) > 0:
                return sum(scores_for_member_with_scores) / len(
                    scores_for_member_with_scores
                )
        return "N/A"

    def __str__(self) -> str:
        return f"{self.name} مربوط به {self.organization}"
