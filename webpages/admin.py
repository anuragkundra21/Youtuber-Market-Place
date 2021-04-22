from django.contrib import admin
from webpages.models import Slider,Team
from django.utils.html import format_html
# Register your models here.
class Slider_Admin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width = "60"/>'.format(object.photo.url))
    list_display=('headline','myphoto','button_text')

class Team_Admin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width = "40"/>'.format(object.photo.url))
    list_display=('id','myphoto','first_name','role','created_at')
    list_display_links=('first_name',)
    search_fields=('first_name','role')
    list_filter=('role',)

admin.site.register(Slider,Slider_Admin)
admin.site.register(Team,Team_Admin)
