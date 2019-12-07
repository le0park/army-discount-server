from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=20, default="", blank=True)
    duty_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.nickname


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    page_url = models.CharField(max_length=255)
    information = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    
    description = models.TextField()
    registration_num = models.CharField(max_length=25)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class PlaceRequest(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(to=Place, on_delete=models.SET_NULL, null=True)
    description = models.TextField(default='')

    # 0: 등록, 1: 처리완료, 2: 반려
    accepted = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description

        
class Like(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(to=Place, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ['user', 'place']


class FavoriteLocation(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(default='', max_length=30)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)