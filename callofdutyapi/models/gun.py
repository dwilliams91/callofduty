from django.db import models

class Gun(models.Model):
     name=models.CharField(max_length=50)
     gun_type=models.CharField(max_length=50)