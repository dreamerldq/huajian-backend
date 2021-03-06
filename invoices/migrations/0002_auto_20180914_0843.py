# Generated by Django 2.1.1 on 2018-09-14 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='invoices.User'),
        ),
    ]
