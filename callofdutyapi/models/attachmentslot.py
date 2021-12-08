from django.db import models


class AttachmentSlot(models.Model):
    name=models.CharField(max_length=50)
    createdclass_id=models.ForeignKey("CreatedClass", on_delete=models.CASCADE)
    attachment_id=models.ForeignKey("Attachment", on_delete=models.CASCADE)
