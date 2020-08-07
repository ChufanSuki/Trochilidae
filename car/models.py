from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import TimeStampedModel
import uuid
class Car_Model(TimeStampedModel):
    """
    A model representing a car model that provides
    ``name``, ``img``, ``code``, ``state``, ``uuid``
    """
    name = models.CharField(max_length=200, help_text='Enter a car model name(e.g. Benz)', verbose_name="Car Model Name")
    img = models.ImageField(verbose_name="Car Model Image")
    code = models.CharField(max_length=50, blank=True, verbose_name="Car Model Code")
    state = models.BooleanField(help_text='Enter 0 or 1.(1=normal,0=delete)', verbose_name="Car Model Status")
    # Used by the API to look up the record
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta(TimeStampedModel.Meta):
        ordering = ['name']

    def __str__(self):
        return f'Model: {self.name}'

    def get_absolute_url(self):
        return reverse('model-detail', args=[str(self.id)])

class Car_User(TimeStampedModel):
    """Model representing the a instance of car model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carModel = models.ForeignKey(Car_Model, on_delete=models.CASCADE)
    mac = models.CharField(max_length=50, help_text="Device MAC Address")
    class StateType(models.IntegerChoices):
        normal = 1
        otherwise = 2
    
    state = models.IntegerField(choices=StateType.choices)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Left blank")

    # class Meta(TimeStampedModel.Meta):
        # permissions = (("can_change_status", "Set car status"),)

    def __str__(self):
        return f'{self.user.username} ({self.carModel.name}) Mac ({self.mac})'

class Car_Check(TimeStampedModel):
    car = models.OneToOneField(Car_User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Left blank")
    
    def __str__(self):
        return '%d %s' % (self.id, self.car.user.username)




