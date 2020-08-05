from django.db import models
from django.contrib.auth.models import User
import uuid

class Images_Info(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particaular image across whole application')
    name = models.CharField(max_length=255)
    height = models.IntegerField(max_length=11)
    width = models.IntegerField(max_length=11)
    size = models.IntegerField(max_length=11)
    extension = models.CharField(max_length=16)
    detail = models.CharField(max_length=500)
    date = models.DateTimeField()
    type = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'uuid: {uuid}'