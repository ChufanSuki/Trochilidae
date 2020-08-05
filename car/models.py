from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

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

    def __str__(self):
        return f'{self.user.username} ({self.carModel.name}) Mac ({self.mac})'

class Riding_Info(models.Model):
    user = models.ForeignKey(Car_User, on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField()
    speed = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
    electric = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    CAR_STATUS = (
        ('s', 'Start'),
        ('e', 'End')
    )
    state = models.CharField(
        max_length=1,
        choices=CAR_STATUS,
        blank=True,
        default='s',
        help_text='State of Car',
    )
    averageSpeed = models.IntegerField(default=0)
    time = models.DateTimeField(help_text="riding time")
    highSpeed = models.CharField(max_length=50)

    class Meta:
        ordering = ['startDate', 'endDate']
    
    def __str__(self):
        return f'{self.id} {self.user.user.username} ({self.user.carModel}) Mac ({self.user.mac}) ({self.startDate}~{self.endDate})'

class Riding_His_Info(models.Model):
    riding = models.OneToOneField(Riding_Info, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def display_mac(self):
        return self.riding.user.mac
    
    display_mac.short_description = 'Mac'

    def display_model(self):
        return self.riding.user.carModel
    
    display_model.short_description = 'Model'

    def display_user(self):
        return self.riding.user.user.username
    
    display_user.short_description = 'Username'

    def display_date(self):
        return f'{self.riding.startDate}~{self.riding.endDate}'
    
    display_date.short_description = 'Date'

    def __str__(self):
        return '%d %s' % (self.id, self.riding.user.user.username)

class Car_Check(models.Model):
    car = models.OneToOneField(Car_User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    date = models.DateTimeField()
    result = models.CharField(max_length=50)

    class Meta:
        ordering = ['date', 'id']
    
    def __str__(self):
        return '%d %s' % (self.id, self.car.user.username)

class Startup_Img(models.Model):
    img = models.ImageField()
    type = models.CharField(max_length=10, default="supercar")
    date = models.DateField(auto_now=True)
    state = models.CharField(max_length=10)

    class Meta:
        ordering = ['date', 'id']

    def __str__(self):
        return '%d' % (self.id)

class Riding_Statistics(models.Model):
    car = models.OneToOneField(Car_User, on_delete=models.CASCADE)
    average_speed = models.IntegerField()
    duration = models.DurationField(help_text="Pleas enter valid format: [dd] [[hh:]mm:]ss")
    max_speed = models.CharField(max_length=50)
    date = models.DateTimeField()

    class Meta:
        ordering = ['car', 'date']
    
    def __str__(self):
        return f'Riding Statistics of {self.car.user.username} created at {self.date}'

class Sms_Codes(models.Model):
    phone_number = PhoneNumberField(primary_key=True)
    code = models.CharField(max_length=10)
    send_date = models.DateTimeField()
    status = models.IntegerField()

    def __str__(self):
        return f'send {self.code} to {self.phone_number} at {self.send_date}'

class System_Config(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=255)
    express = models.CharField(max_length=4096, blank=True)
    type = models.IntegerField()
    note = models.CharField(max_length=4096, blank=True)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.name}:{self.value}'




