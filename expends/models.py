from django.db import models

from users.models import User
# Create your models here.

class Expend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_principle = models.CharField(max_length=20)
    expend_content = models.CharField(max_length=100, null=True)
    expend_money = models.FloatField()
    project_name = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    create_time = models.DateTimeField(null=True)
    state = models.BooleanField(default=False, null=True)

# 创建支出项目
