from django.db import models
from datetime import datetime
# Create your models here.

class Hiretuber(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tubers_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    tubers_id = models.IntegerField()
    users_id = models.IntegerField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(blank=True,default=datetime.now())

    def __str__(self):
        return self.email
