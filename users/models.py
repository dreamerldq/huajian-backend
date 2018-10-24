from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30, default='123456')
    phone_number = models.IntegerField(null=True)
    create_time = models.DateTimeField()

# 创建项目负责人
