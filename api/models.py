import uuid
from django.db import models

class UUIDValue(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
