from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Wine(models.Model):
    title = models.CharField(max_length=100)
    winery = models.CharField(max_length=100)
    img = models.CharField(max_length=1000, blank=True)
    price = models.IntegerField(default=0)
    date_consumed = models.DateField(default=date.today)
    review = models.CharField(max_length=500, blank=True)
    rating = models.FloatField(default=5)
    variety = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    where_purchased = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(
        User, related_name='wines', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
