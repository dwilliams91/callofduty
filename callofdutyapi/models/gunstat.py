from django.db import models

class GunStat(models.Model):
    gun_id=models.ForeignKey("Gun")
    stat_id=models.CharField("Stat")
    value=models.DecimalField(max_digits=6)