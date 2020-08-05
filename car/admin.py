from django.contrib import admin
from django.contrib.auth.models import User
from .models import Car_User, Car_Model, Riding_Info, Riding_His_Info, Car_Check, Startup_Img, Riding_Statistics, Sms_Codes, System_Config


class CarsInstanceInline(admin.TabularInline):
    model = Car_User
    extra = 0

@admin.register(Car_User)
class Car_UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'carModel', 'date', 'mac', 'state')
    list_filter = ('user', 'carModel', 'date', 'mac', 'state')

    fieldsets = (
        (None, {
            'fields': ('user', )
        }),
        ('Car', {
            'fields': ('carModel', 'mac', 'state')
        }),
    )


@admin.register(Car_Model)
class Car_ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'state', 'img')
    inlines = [CarsInstanceInline]

@admin.register(Riding_Info)
class Riding_InfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'startDate', 'endDate')

@admin.register(Riding_His_Info)
class Riding_His_InfoAdmin(admin.ModelAdmin):
    list_display = ('display_user', 'display_mac', 'display_model', 'display_date')

@admin.register(Car_Check)
class Car_CheckAdmin(admin.ModelAdmin):
    list_display = ('car', 'type', 'date', 'result')

@admin.register(Startup_Img)
class Startup_ImgAdmin(admin.ModelAdmin):
    pass

@admin.register(Riding_Statistics)
class Riding_StatisticsAdmin(admin.ModelAdmin):
    list_display = ('car', 'duration', 'date', 'max_speed', 'average_speed')

@admin.register(Sms_Codes)
class Sms_CodesAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'send_date', 'status')

@admin.register(System_Config)
class System_ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'express', 'type', 'note', 'status')
