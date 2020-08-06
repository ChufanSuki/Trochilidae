from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Startup_Img(models.Model):
    img = models.ImageField()
    type = models.CharField(max_length=10, default="supercar")
    date = models.DateField(auto_now=True)
    state = models.CharField(max_length=10)

    class Meta:
        ordering = ['date', 'id']

    def __str__(self):
        return '%d' % (self.id)

class Sms_Codes(models.Model):
    phone_number = PhoneNumberField(primary_key=True)
    code = models.CharField(max_length=10)
    send_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField()

    def __str__(self):
        return f'send {self.code} to {self.phone_number} at {self.send_date}'

class System_Config(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=255)
    express = models.CharField(max_length=4096, blank=True, help_text="Config Express")
    type = models.IntegerField()
    note = models.CharField(max_length=4096, blank=True)
    status = models.BooleanField(help_text="true for normal status")

    def __str__(self):
        return f'{self.name}:{self.value}'

