from django.db import models

class CreatedClass(models.model):
    name=models.CharField(max_length=50)
    base_gun=models.ForeignKey("Gun")