from django.db import models

class CreatedClass(models.Model):
    name=models.CharField(max_length=50)
    base_gun=models.ForeignKey("Gun", on_delete=models.CASCADE)