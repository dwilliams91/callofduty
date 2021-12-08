from django.db import models

class AttachmentStat(models.Model):
    attachment_id=models.ForeignKey("Attachment", on_delete=models.CASCADE)
    stat_id=models.ForeignKey("Stat", on_delete=models.CASCADE)
    effect=models.DecimalField(max_digits=4, decimal_places=3)