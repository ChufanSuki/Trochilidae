from django.db import models
from car.models import Car_Model, Car_User

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
