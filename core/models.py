from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Conference(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(default='00:00')
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title