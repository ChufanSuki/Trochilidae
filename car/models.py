from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Car_Model(models.Model):
    """Model representing a car."""
    name = models.CharField(max_length=200, help_text='Enter a car model name(e.g. Benz)')
    img = models.ImageField()
    code = models.CharField(max_length=50, blank=True)
    state = models.BooleanField(help_text='Enter 0 or 1.(1=normal,0=delete)')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('model-detail', args=[str(self.id)])

class Car_User(models.Model):
    """Model representing the a instance of car model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carModel = models.ForeignKey(Car_Model, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    mac = models.CharField(max_length=50)
    state = models.IntegerField()


    class Meta:
        ordering = ['date', 'id']
        permissions = (("can_change_status", "Set car status"),)

    def __str__(self):
        return f'{self.user.username} ({self.carModel.name}) Mac ({self.mac})'

class Car_Check(models.Model):
    car = models.OneToOneField(Car_User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    date = models.DateTimeField()
    result = models.CharField(max_length=50)

    class Meta:
        ordering = ['date', 'id']
    
    def __str__(self):
        return '%d %s' % (self.id, self.car.user.username)




