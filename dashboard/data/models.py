from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Data(models.Model):
    timestamp = models.IntegerField()
    node = models.CharField(default='other', max_length=40)
    datetime = models.DateField()
    gps_lat = models.FloatField()
    gps_lng = models.FloatField()
    gps_alt = models.IntegerField()
    pm1 = models.IntegerField()
    pm10 = models.IntegerField()
    pm2_5 = models.IntegerField()
    airpressure = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return self.datetime
