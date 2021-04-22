from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Youtuber(models.Model):
    crew_choices=(
        ('solo','solo'),
        ('large','large'),
        ('small','small'),
    )

    camera_choices=(
        ('canon','canon'),
        ('nikon','nikon'),
        ('panasonic','panasonic'),
        ('red','red'),
        ('sony','sony'),
        ('other','other'),
    )

    category_choices=(
        ('code','code'),
        ('comedy','comedy'),
        ('cooking','cooking'),
        ('vlogs','vlogs'),
        ('gaming','gaming'),
        ('film_makings','film_makings'),
    )
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='media/ytubers/%Y/%m')
    video_url=models.CharField(max_length=255)
    description=RichTextField()
    city=models.CharField(max_length=255)
    age=models.IntegerField()
    category=models.CharField(choices=category_choices,max_length=255)
    subs_count=models.CharField(max_length=255)
    crew=models.CharField(choices=crew_choices,max_length=255)
    is_featured=models.BooleanField(default=False)
    height=models.IntegerField()
    camera_type=models.CharField(choices=camera_choices,max_length=255)
    created_at=models.DateTimeField(default=datetime.now,blank=True)
