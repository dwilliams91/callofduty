from django.db import models


class AttachmentSlot(models.Model):
    name=models.CharField(max_length=50)
    createdclass_id=models.ForeignKey("CreatedClass")
    attachment_id=models.ForeignKey("Attachment")

#%%
import pandas as pd
# %%
