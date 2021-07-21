from django.db import models
from hashid_field.field import HashidAutoField
from .organization import Organization


class Team(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(
        to=Organization, related_name="teams", on_delete=models.DO_NOTHING
    )

    def __str__(self) -> str:
        return f"{self.name} مربوط به {self.organization}"
