from django.contrib import admin
from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
from .models import Car_User, Car_Model, Car_Check


# This is auto done by django: 
# admin.site.register(User, UserAdmin)

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

@admin.register(Car_Check)
class Car_CheckAdmin(admin.ModelAdmin):
    list_display = ('car', 'type', 'date', 'result')

