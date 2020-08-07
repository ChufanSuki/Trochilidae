from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from core.models import TimeStampedModel
import uuid
class Startup_Img(TimeStampedModel):
    img = models.ImageField()
    type = models.CharField(max_length=10, default="supercar")
    state = models.CharField(max_length=10)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Left blank")
    
    def __str__(self):
        return f'{self.id}'

class Sms_Codes(TimeStampedModel):
    phone_number = PhoneNumberField(primary_key=True)
    code = models.CharField(max_length=10)
    send_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField()
    uuid = models.UUIDField(default=uuid.uuid4, help_text="Left blank")

    def __str__(self):
        return f'send {self.code} to {self.phone_number} at {self.send_date}'

class System_Config(TimeStampedModel):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=255)
    express = models.CharField(max_length=4096, blank=True, help_text="Config Express")
    type = models.IntegerField()
    note = models.CharField(max_length=4096, blank=True)
    status = models.BooleanField(help_text="true for normal status")
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Left blank")

    def __str__(self):
        return f'{self.name}:{self.value}'

