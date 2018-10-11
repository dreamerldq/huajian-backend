from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    create_time = models.DateTimeField()


class Invoice(models.Model):
    invoice_type = models.CharField(max_length=10)
    money = models.FloatField()
    project_principle = models.CharField(max_length=20)
    project_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    taxpayer_id = models.IntegerField(unique=True)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    bank = models.CharField(max_length=100)
    bank_user = models.IntegerField()
    remark = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.project_principle


class AccountList(models.Model):
     invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
     money_received = models.FloatField()
     money_receivable = models.FloatField()
     pay_type = models.CharField(max_length=5)
     remark = models.CharField(max_length=100)
     create_time = models.DateTimeField(null=True)



