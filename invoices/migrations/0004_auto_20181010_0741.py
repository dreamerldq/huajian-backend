# Generated by Django 2.1.1 on 2018-10-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_auto_20180914_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='project_principle',
            field=models.CharField(max_length=20),
        ),
    ]
