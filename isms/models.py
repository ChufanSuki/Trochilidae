from django.db import models
from django.contrib.auth.models import User
import uuid
from core.models import TimeStampedModel

class Images_Info(TimeStampedModel):
    PNG = 'PNG'
    JPEG = 'JPEG'
    GIF = 'GIF'
    BMP = 'BMP'
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particaular image across whole application')
    name = models.CharField(max_length=255)
    height = models.IntegerField()
    width = models.IntegerField()
    size = models.IntegerField()
    IMAGE_EXTENSION_CHOICES = [
        (PNG, '.png'),
        (JPEG, '.jpeg'),
        (GIF, '.gif'),
        (BMP, '.bmp'),
    ]
    extension = models.CharField(max_length=4, choices=IMAGE_EXTENSION_CHOICES)
    detail = models.CharField(max_length=500)
    class CreateType(models.IntegerChoices):
        upload_by_web = 300
        upload_by_app = 200
    type = models.IntegerField(choices=CreateType.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'uuid: {self.uuid}'