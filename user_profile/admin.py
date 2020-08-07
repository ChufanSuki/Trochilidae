from django.contrib import admin
from .models import UserProfile, MaintainerProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'uuid', 'mobile')
    exclude = ('uuid',)


@admin.register(MaintainerProfile)
class MaintainerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'uuid')
    exclude = ('uuid',)