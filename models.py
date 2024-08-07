from django.db import models

# Create your models here.

class stockmarket(models.Model):
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()