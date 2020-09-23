import datetime

from django.db import models
from django.utils import timezone

class Comic(models.Model):
    title = models.CharField(max_length=100)
    URI = models.CharField(max_length=100)
    alt_text = models.CharField(max_length = 400)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title