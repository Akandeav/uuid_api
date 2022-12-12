import uuid
from django.db import models

class UUIDValue(models.Model):
    time_stamp = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4)
