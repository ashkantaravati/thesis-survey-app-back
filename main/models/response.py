from django.db import models
from main.calculations import round_as_default

from .team import Team
from django.contrib.admin import display
from hashid_field.field import HashidAutoField
from main.typing import ICCFrameRecord, ListOfICCFrameRecord

SEX_CHOICES = [("male", "آقا"), ("female", "خانم")]


class Response(models.Model):
    id = HashidAutoField(primary_key=True)
    team = models.ForeignKey(
        to=Team, related_name="responses", on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # General Survey
    age = models.IntegerField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=6)
    tenure = models.FloatField(default=0.0)
    team_history = models.IntegerField(default=0)

    # Overconfidence Survey
    overconfidence_question_one_lower = models.IntegerField()
    overconfidence_question_one_upper = models.IntegerField()
    overconfidence_question_two_lower = models.IntegerField()
    overconfidence_question_two_upper = models.IntegerField()
    overconfidence_question_three_lower = models.IntegerField()
    overconfidence_question_three_upper = models.IntegerField()
    overconfidence_question_four_lower = models.IntegerField()
    overconfidence_question_four_upper = models.IntegerField()
    overconfidence_question_five_lower = models.IntegerField()
    overconfidence_question_five_upper = models.IntegerField()
    overconfidence_question_six_lower = models.IntegerField()
    overconfidence_question_six_upper = models.IntegerField()
    overconfidence_question_seven_lower = models.IntegerField()
    overconfidence_question_seven_upper = models.IntegerField()
    overconfidence_question_eight_lower = models.IntegerField()
    overconfidence_question_eight_upper = models.IntegerField()
    overconfidence_question_nine_lower = models.IntegerField()
    overconfidence_question_nine_upper = models.IntegerField()
    overconfidence_question_ten_lower = models.IntegerField()
    overconfidence_question_ten_upper = models.IntegerField()
    # Team Coordination Survey
    team_coordination_question_one = models.IntegerField()
    team_coordination_question_two = models.IntegerField()
    team_coordination_question_three = models.IntegerField()
    team_coordination_question_four = models.IntegerField()
    team_coordination_question_five = models.IntegerField()

    # Team Effonectiveness Survey
    team_effectiveness_question_one = models.IntegerField()
    team_effectiveness_question_two = models.IntegerField()
    team_effectiveness_question_three = models.IntegerField()
    team_effectiveness_question_four = models.IntegerField()
    team_effectiveness_question_five = models.IntegerField()
    team_effectiveness_question_six = models.IntegerField()
    team_effectiveness_question_seven = models.IntegerField()
    team_effectiveness_question_eight = models.IntegerField()
    team_effectiveness_question_nine = models.IntegerField()
    team_effectiveness_question_ten = models.IntegerField()
    # Voice Survey
    voice_question_one = models.IntegerField()
    voice_question_two = models.IntegerField()
    voice_question_three = models.IntegerField()
    voice_question_four = models.IntegerField()
    voice_question_five = models.IntegerField()
    voice_question_six = models.IntegerField()
    #
    feedback = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Response from {self.team.name}"

    @property
    @display(
        description="Overconfidence Score",
    )
    def overconfidence_score(self) -> float:
        pass

    @property
    @display(
        description="Team Coordination Score",
    )
    def team_coordination_score(self) -> float:
        return round_as_default(
            (
                self.team_coordination_question_one
                + self.team_coordination_question_two
                + self.team_coordination_question_three
                + self.team_coordination_question_four
                + self.team_coordination_question_five
            )
            / 5
        )

    @property
    @display(
        description="Team Effectiveness Score",
    )
    def team_effectiveness_score(self) -> float:
        return round_as_default(
            (
                self.team_effectiveness_question_one
                + self.team_effectiveness_question_two
                + self.team_effectiveness_question_three
                + self.team_effectiveness_question_four
                + self.team_effectiveness_question_five
                + self.team_effectiveness_question_six
                + self.team_effectiveness_question_seven
                + self.team_effectiveness_question_eight
                + self.team_effectiveness_question_nine
                + self.team_effectiveness_question_ten
            )
            / 10
        )

    @property
    @display(
        description="Voice Score",
    )
    def voice_behavior_score(self) -> float:
        return round_as_default(
            (
                self.voice_question_one
                + self.voice_question_two
                + self.voice_question_three
                + self.voice_question_four
                + self.voice_question_five
                + self.voice_question_six
            )
            / 6
        )

    def team_coordination_as_record(self) -> ICCFrameRecord:
        return (
            self.id.hashid,
            self.team.id.hashid,
            self.team_coordination_score,
        )

    def team_effectiveness_as_record(self) -> ICCFrameRecord:
        return (
            self.id.hashid,
            self.team.id.hashid,
            self.team_effectiveness_score,
        )
