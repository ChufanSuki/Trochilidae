from django.contrib import admin
from .models import Riding_Info, Riding_His_Info, Riding_Statistics

@admin.register(Riding_Info)
class Riding_InfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'startDate', 'endDate')
    exclude = ('uuid', )

@admin.register(Riding_His_Info)
class Riding_His_InfoAdmin(admin.ModelAdmin):
    list_display = ('display_user', 'display_mac', 'display_model', 'display_date') 
    exclude = ('uuid', )

@admin.register(Riding_Statistics)
class Riding_StatisticsAdmin(admin.ModelAdmin):
    list_display = ('car', 'duration', 'date', 'max_speed', 'average_speed', 'created', 'modified')
    exclude = ('uuid', )
