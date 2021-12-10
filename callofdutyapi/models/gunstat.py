from django.db import models

class GunStat(models.Model):
    gun_id=models.ForeignKey("Gun", on_delete=models.CASCADE)
    stat_id=models.ForeignKey("Stat", on_delete=models.CASCADE)
    value=models.DecimalField(max_digits=10, decimal_places=4)
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter 
    def joined(self, value):
        self.__joined = value