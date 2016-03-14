from django.db import models
from django.conf import settings


class Pair(models.Model):
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)

    def __str__(self):
        return '{} or {}'.format(self.a, self.b)


class Choice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    # True if User chose pair.a, False if User chose pair.b
    choice = models.BooleanField()

    def __str__(self):
        return '{} ({})'.format(self.pair, self.choice)
