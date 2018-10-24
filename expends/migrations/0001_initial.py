# Generated by Django 2.1.1 on 2018-10-24 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_principle', models.CharField(max_length=20)),
                ('expend_content', models.CharField(max_length=100, null=True)),
                ('expend_money', models.FloatField()),
                ('project_name', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(null=True)),
                ('state', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
