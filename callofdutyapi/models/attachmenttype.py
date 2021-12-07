from django.db import models


class AttachmentType(models.Model):
    name=models.CharField(max_length=50)
    
