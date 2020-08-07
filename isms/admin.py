from django.contrib import admin
from .models import Images_Info

@admin.register(Images_Info)
class Images_InfoAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'height', 'width', 'size', 'extension', 'detail', 'created', 'modified', 'type', 'user')
    exclude = ('created', 'modified', 'uuid')
