# Generated by Django 2.1.1 on 2018-10-10 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_auto_20181010_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='create_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
