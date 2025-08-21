from django.contrib import admin
from .models import Aboutus

class AboutusAdmin(admin.ModelAdmin):
    list_display=['title','about']

admin. site.register(Aboutus,AboutusAdmin)

# Register your models here.
