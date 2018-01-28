from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    class Meta:
        db_table = "user_profile"

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,null=True)
    wechat_id = models.CharField(max_length=50,null=True)



class Toy(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    buy_date = models.DateField()