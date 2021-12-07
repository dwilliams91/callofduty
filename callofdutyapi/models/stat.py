from django.db import models

class Stat(models.Model):
    name=models.CharField(max_length=50)
    unit=models.CharField(max_length=50)