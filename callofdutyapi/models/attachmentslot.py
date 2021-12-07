from django.db import models

class Attachment(models.Model):
    name=models.CharField(max_length=50)