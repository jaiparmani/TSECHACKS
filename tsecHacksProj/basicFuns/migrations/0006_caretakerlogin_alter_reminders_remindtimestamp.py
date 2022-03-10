# Generated by Django 4.0.3 on 2022-03-10 01:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicFuns', '0005_auto_20220310_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaretakerLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='reminders',
            name='remindTimeStamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 6, 41, 27, 294398)),
        ),
    ]
