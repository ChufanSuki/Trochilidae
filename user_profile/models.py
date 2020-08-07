from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics', help_text="avatar")
    class SexType(models.IntegerChoices):
        male = 1
        female = 0
        sercet = -1
    sex = models.IntegerField(choices=SexType.choices)
    lastIp = models.GenericIPAddressField(verbose_name="Last Login IP")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Left blank")

    class Meta():
        abstract = True

    def __str__(self):
        return f'{self.user.username} Profile'

class UserProfile(Profile):
    nickname = models.CharField(max_length=50, blank=True)
    mobile = PhoneNumberField(blank=True)
    address = models.CharField(max_length=50, blank=True)
    birthday = models.DateTimeField(blank=True)
    company = models.CharField(max_length=50, help_text="Your company name.e.g. Google", blank=True)
    role = models.CharField(max_length=50, blank=True)
    rankId = models.IntegerField(default=0)
    money = models.FloatField(default=0)
    points = models.IntegerField(default=0)
    question = models.CharField(max_length=50, blank=True, help_text="Security Question.e.g. Where were I born?", verbose_name="Security Question")
    answer = models.CharField(max_length=50, blank=True, help_text="Answer to Security Question.")



class MaintainerProfile(Profile):
    name = models.CharField(max_length=50, verbose_name="Real Name")
