from django.contrib import admin
from .models import Car_User, Car_Model, Riding_Info, Riding_His_Info, Car_Check, Startup_Img, Riding_Statistics, Sms_Codes, System_Config

@admin.register(Car_User)
class Car_UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'carModel', 'date', 'mac', 'state')

@admin.register(Car_Model)
class Car_ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'state', 'img')

@admin.register(Riding_Info)
class Riding_InfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'startDate', 'endDate')

@admin.register(Riding_His_Info)
class Riding_His_InfoAdmin(admin.ModelAdmin):
    list_display = ('riding', )

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

# admin.site.register(Car_User)
# admin.site.register(Car_Model)
# admin.site.register(Riding_Info)
# admin.site.register(Riding_His_Info)
# admin.site.register(Car_Check)
# admin.site.register(Startup_Img)
# admin.site.register(Riding_Statistics)
# admin.site.register(Sms_Codes)
# admin.site.register(System_Config)