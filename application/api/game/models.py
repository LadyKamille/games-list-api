from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return self.title
