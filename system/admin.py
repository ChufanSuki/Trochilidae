from django.contrib import admin
from .models import Startup_Img, Sms_Codes, System_Config

@admin.register(Startup_Img)
class Startup_ImgAdmin(admin.ModelAdmin):
    list_display = ('img', 'type', 'created', 'state')

@admin.register(Sms_Codes)
class Sms_CodesAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'send_date', 'status')

@admin.register(System_Config)
class System_ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'express', 'type', 'note', 'status')
