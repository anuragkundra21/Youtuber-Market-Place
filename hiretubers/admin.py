from django.contrib import admin
from .models import  Hiretuber
# Register your models here.

class HTAdmin(admin.ModelAdmin):
    list_display=('first_name','email','tubers_name')
    
admin.site.register(Hiretuber,HTAdmin)
