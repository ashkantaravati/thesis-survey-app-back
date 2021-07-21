from django.db import models
from hashid_field.field import HashidAutoField


class Organization(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Organization's Name")
    rep_name = models.CharField(max_length=50)
    rep_email = models.EmailField(null=True, blank=True)
    rep_job_title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} "
