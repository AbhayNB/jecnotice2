from django.contrib import admin
from .models import ENotice
# Register your models here.
class EnoticeAdmin(admin.ModelAdmin):
    list_display=['Topic','Name','File','Disc']
admin.site.register(ENotice,EnoticeAdmin)