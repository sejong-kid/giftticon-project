from unittest.util import _MAX_LENGTH
from django.db import models


class Giftmodel(models.Model):
    giftname=models.CharField(max_length = 100)
    maxdate=models.IntegerField()
    pinnum = models.IntegerField()
    theme=models.CharField(max_length = 100)
    themeimg=models.CharField(max_length = 100)
    class Meta:
        db_table = 'Giftmodel'