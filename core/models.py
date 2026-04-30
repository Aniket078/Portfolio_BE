from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    hp = models.IntegerField(default=100)
    mp = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name