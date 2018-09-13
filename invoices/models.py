from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Invoice(models.Model):
    invoice_type = models.CharField(max_length=10)
    money = models.FloatField()
    project_principle = models.CharField(max_length=20, unique=True)
    project_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, unique=True)
    taxpayer_id = models.IntegerField(unique=True)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    bank = models.CharField(max_length=100)
    bank_user = models.IntegerField()
    remark = models.CharField(max_length=100)

    def __str__(self):
        return self.project_principle



