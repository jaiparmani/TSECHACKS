# Generated by Django 3.0.6 on 2022-03-09 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicFuns', '0003_auto_20220309_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminders',
            name='remindTimeStamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 0, 6, 25, 16818)),
        ),
    ]