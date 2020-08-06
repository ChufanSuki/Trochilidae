from django.contrib import admin
from .models import UserProfile, MaintainerProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(MaintainerProfile)
