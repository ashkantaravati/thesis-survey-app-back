from django.db import models
from hashid_field.field import HashidAutoField

SEX_CHOICES = [("male", "آقا"), ("female", "خانم")]


class Organization(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Organization's Name")
    rep_name = models.CharField(max_length=50)
    rep_email = models.EmailField()
    rep_job_title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"


class Team(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(
        to=Organization, related_name="teams", on_delete=models.DO_NOTHING
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.id} | {self.organization}"


class ParticipantTeamMember(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10, null=True, blank=True)
    team = models.ForeignKey(
        to=Team, related_name="members", on_delete=models.DO_NOTHING
    )
    organization = models.ForeignKey(to=Organization, on_delete=models.DO_NOTHING)
    overconfidence_question_1_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_1_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_2_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_2_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_3_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_3_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_4_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_4_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_5_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_5_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_6_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_6_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_7_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_7_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_8_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_8_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_9_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_9_max = models.IntegerField(null=True, blank=True)
    overconfidence_question_10_min = models.IntegerField(null=True, blank=True)
    overconfidence_question_10_max = models.IntegerField(null=True, blank=True)
    team_coordination_question_1 = models.IntegerField(null=True, blank=True)
    team_coordination_question_2 = models.IntegerField(null=True, blank=True)
    team_coordination_question_3 = models.IntegerField(null=True, blank=True)
    team_coordination_question_4 = models.IntegerField(null=True, blank=True)
    team_coordination_question_5 = models.IntegerField(null=True, blank=True)


class TeamMemberVoiceEvaluationByParticipant(models.Model):
    voice_question_1 = models.IntegerField()
    voice_question_2 = models.IntegerField()
    voice_question_3 = models.IntegerField()
    voice_question_4 = models.IntegerField()
    voice_question_5 = models.IntegerField()
    voice_question_6 = models.IntegerField()
    evaluating_participant = models.ForeignKey(
        to=ParticipantTeamMember,
        on_delete=models.DO_NOTHING,
        related_name="evaluating_participant",
    )
    evaluated_participant = models.ForeignKey(
        to=ParticipantTeamMember,
        on_delete=models.DO_NOTHING,
        related_name="evaluated_participant",
    )
    team = models.ForeignKey(to=Team, on_delete=models.DO_NOTHING)
