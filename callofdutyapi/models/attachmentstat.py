from django.db import models

class AttachmentStat(models.Model):
    attachment_id=models.ForeignKey("Attachment")
    stat_id=models.ForeignKey("Stat")
    effect=models.DecimalField(max_digits=4)