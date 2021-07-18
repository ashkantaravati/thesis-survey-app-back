from django.db import models
from hashid_field.field import HashidAutoField

SEX_CHOICES = [("male", "آقا"), ("female", "خانم")]


class Organization(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Organization's Name")
    rep_name = models.CharField(max_length=50)
    rep_email = models.EmailField(null=True, blank=True)
    rep_job_title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} "


class Team(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(
        to=Organization, related_name="teams", on_delete=models.DO_NOTHING
    )

    def __str__(self) -> str:
        return f"{self.name} مربوط به {self.organization}"


class ParticipantTeamMember(models.Model):
    id = HashidAutoField(primary_key=True)
    has_participated = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    team = models.ForeignKey(
        to=Team, related_name="members", on_delete=models.DO_NOTHING
    )
    organization = models.ForeignKey(to=Organization, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.name} از تیم {self.team}"


class GeneralSurveyResponse(models.Model):
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10, null=True, blank=True)
    # TODO add tenure and team history
    participant = models.OneToOneField(
        to=ParticipantTeamMember,
        on_delete=models.CASCADE,
        related_name="general_survey_response",
    )

    def __str__(self):
        return f"پرسش‌های عمومی مربوط به {self.participant}  "


class OverconfidenceSurveyResponse(models.Model):
    question_1_min = models.IntegerField(null=True, blank=True)
    question_1_max = models.IntegerField(null=True, blank=True)
    question_2_min = models.IntegerField(null=True, blank=True)
    question_2_max = models.IntegerField(null=True, blank=True)
    question_3_min = models.IntegerField(null=True, blank=True)
    question_3_max = models.IntegerField(null=True, blank=True)
    question_4_min = models.IntegerField(null=True, blank=True)
    question_4_max = models.IntegerField(null=True, blank=True)
    question_5_min = models.IntegerField(null=True, blank=True)
    question_5_max = models.IntegerField(null=True, blank=True)
    question_6_min = models.IntegerField(null=True, blank=True)
    question_6_max = models.IntegerField(null=True, blank=True)
    question_7_min = models.IntegerField(null=True, blank=True)
    question_7_max = models.IntegerField(null=True, blank=True)
    question_8_min = models.IntegerField(null=True, blank=True)
    question_8_max = models.IntegerField(null=True, blank=True)
    question_9_min = models.IntegerField(null=True, blank=True)
    question_9_max = models.IntegerField(null=True, blank=True)
    question_10_min = models.IntegerField(null=True, blank=True)
    question_10_max = models.IntegerField(null=True, blank=True)
    participant = models.OneToOneField(
        to=ParticipantTeamMember,
        on_delete=models.CASCADE,
        related_name="overconfidence_survey_response",
    )


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

    def __str__(self) -> str:
        return f"نظر {self.evaluating_participant} درباره‌ی رفتار صدای {self.evaluated_participant}"
