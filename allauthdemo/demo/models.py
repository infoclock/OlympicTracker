from django.db import models


class Problem(models.Model):
    link = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
