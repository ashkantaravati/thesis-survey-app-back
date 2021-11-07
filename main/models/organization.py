from django.db import models
from hashid_field.field import HashidAutoField
from django.contrib.admin import display


class Organization(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Organization's Name")
    rep_name = models.CharField(max_length=50)
    rep_email = models.EmailField(null=True, blank=True)
    rep_job_title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    @display(
        description="Number of Teams",
    )
    def number_of_teams(self):
        return self.teams.count()

    @property
    def number_of_participated_teams(self):
        participated_teams = [
            team for team in self.teams.all() if team.has_participated
        ]
        return len(participated_teams)

    @property
    def has_participated(self):
        return self.number_of_participated_teams > 0

    def __str__(self) -> str:
        return f"{self.name} "
