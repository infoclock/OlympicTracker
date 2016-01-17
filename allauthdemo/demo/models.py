from django.db import models
from allauthdemo.auth.models import DemoUser


class Problem(models.Model):
    link = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name


class ContestParticipation(models.Model):
    user = models.ForeignKey(DemoUser, null=True)
    score = models.PositiveSmallIntegerField(default=0)
    place = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=200)
