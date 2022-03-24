from random import choices
from django.db import models
from main.calculations import determine_overconfidence_score, round_as_default
from main.constants import (
    OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE,
    OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS,
    OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
    SEX_CHOICES,
)

from .team import Team
from django.contrib.admin import display
from hashid_field.field import HashidAutoField
from main.typing import ICCFrameRecord, ListOfICCFrameRecord


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
    overconfidence_question_one_lower = models.IntegerField(
        verbose_name="کشور ایران در حال حاضر (سال ۱۴۰۰) چند استان دارد؟"
    )
    overconfidence_question_one_upper = models.IntegerField()
    overconfidence_question_one_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (31)",
    )
    overconfidence_question_two_lower = models.IntegerField(
        verbose_name="در چه سالی تلفن همراه اپل با نام iPhone برای اولین بار عرضه شد؟"
    )
    overconfidence_question_two_upper = models.IntegerField()
    overconfidence_question_two_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (2007 | 1386-7)",
    )
    overconfidence_question_three_lower = models.IntegerField(
        verbose_name="در اروپا چند کشور وجود دارد (که سازمان ملل به رسمیت می‌شناسد)؟"
    )
    overconfidence_question_three_upper = models.IntegerField()
    overconfidence_question_three_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (44)",
    )
    overconfidence_question_four_lower = models.IntegerField(
        verbose_name="ویندوز XP در چه سالی عرضه شد؟"
    )
    overconfidence_question_four_upper = models.IntegerField()
    overconfidence_question_four_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (2000 | 1380)",
    )
    overconfidence_question_five_lower = models.IntegerField(
        verbose_name="چند کشور در آمریکای شمالی وجود دارد؟"
    )
    overconfidence_question_five_upper = models.IntegerField()
    overconfidence_question_five_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (23)",
    )
    overconfidence_question_six_lower = models.IntegerField(
        verbose_name="وب جهانی (WWW) در چه سالی اختراع شد؟"
    )
    overconfidence_question_six_upper = models.IntegerField()
    overconfidence_question_six_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (1989 | 1368)",
    )
    overconfidence_question_seven_lower = models.IntegerField(
        verbose_name="اولین موتور جستجوی وب در چه سالی ساخته شد؟"
    )
    overconfidence_question_seven_upper = models.IntegerField()
    overconfidence_question_seven_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (1993~1998 | 1371~1377)",
    )
    overconfidence_question_eight_lower = models.IntegerField(
        verbose_name="انسان بالغ به طور میانگین چند دندان دارد؟"
    )
    overconfidence_question_eight_upper = models.IntegerField()
    overconfidence_question_eight_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (32)",
    )
    overconfidence_question_nine_lower = models.IntegerField(
        verbose_name="مسافت تهران تا مشهد چند کیلومتر است؟"
    )
    overconfidence_question_nine_upper = models.IntegerField()
    overconfidence_question_nine_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (899~926)",
    )
    overconfidence_question_ten_lower = models.IntegerField(
        verbose_name="قدمت (سن) برج آزادی تهران چند سال است؟"
    )
    overconfidence_question_ten_upper = models.IntegerField()
    overconfidence_question_ten_outcome = models.IntegerField(
        choices=OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES,
        null=True,
        blank=True,
        verbose_name="Outcome (50)",
    )
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

    def get_overconfidence_quiz_responses_as_tuples(self):
        return [
            (
                (
                    self.overconfidence_question_one_lower,
                    self.overconfidence_question_one_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[1],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[1],
            ),
            (
                (
                    self.overconfidence_question_two_lower,
                    self.overconfidence_question_two_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[2],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[2],
            ),
            (
                (
                    self.overconfidence_question_three_lower,
                    self.overconfidence_question_three_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[3],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[3],
            ),
            (
                (
                    self.overconfidence_question_four_lower,
                    self.overconfidence_question_four_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[4],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[4],
            ),
            (
                (
                    self.overconfidence_question_five_lower,
                    self.overconfidence_question_five_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[5],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[5],
            ),
            (
                (
                    self.overconfidence_question_six_lower,
                    self.overconfidence_question_six_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[6],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[6],
            ),
            (
                (
                    self.overconfidence_question_seven_lower,
                    self.overconfidence_question_seven_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[7],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[7],
            ),
            (
                (
                    self.overconfidence_question_eight_lower,
                    self.overconfidence_question_eight_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[8],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[8],
            ),
            (
                (
                    self.overconfidence_question_nine_lower,
                    self.overconfidence_question_nine_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[9],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[9],
            ),
            (
                (
                    self.overconfidence_question_ten_lower,
                    self.overconfidence_question_ten_upper,
                ),
                OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE[10],
                OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS[10],
            ),
        ]

    @property
    @display(
        description="Overconfidence Score",
    )
    def overconfidence_score(self) -> float:
        questions = self.get_overconfidence_quiz_responses_as_tuples()
        scores = [
            determine_overconfidence_score(minmax, range, correct_answer)
            for (minmax, range, correct_answer) in questions
        ]
        return sum(scores)

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

    def team_coordination_as_record_per_question(self) -> ListOfICCFrameRecord:
        return [
            (self.id.hashid, "q1", self.team_coordination_question_one),
            (self.id.hashid, "q2", self.team_coordination_question_two),
            (self.id.hashid, "q3", self.team_coordination_question_three),
            (self.id.hashid, "q4", self.team_coordination_question_four),
            (self.id.hashid, "q5", self.team_coordination_question_five),
        ]

    def team_effectiveness_as_record(self) -> ICCFrameRecord:
        return (
            self.id.hashid,
            self.team.id.hashid,
            self.team_effectiveness_score,
        )

    def team_effectiveness_as_record_per_question(self) -> ListOfICCFrameRecord:
        return [
            (self.id.hashid, "q1", self.team_effectiveness_question_one),
            (self.id.hashid, "q2", self.team_effectiveness_question_two),
            (self.id.hashid, "q3", self.team_effectiveness_question_three),
            (self.id.hashid, "q4", self.team_effectiveness_question_four),
            (self.id.hashid, "q5", self.team_effectiveness_question_five),
            (self.id.hashid, "q6", self.team_effectiveness_question_six),
            (self.id.hashid, "q7", self.team_effectiveness_question_seven),
            (self.id.hashid, "q8", self.team_effectiveness_question_eight),
            (self.id.hashid, "q9", self.team_effectiveness_question_nine),
            (self.id.hashid, "q10", self.team_effectiveness_question_ten),
        ]
