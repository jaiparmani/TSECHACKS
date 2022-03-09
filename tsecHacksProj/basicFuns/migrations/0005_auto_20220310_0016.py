# Generated by Django 3.0.6 on 2022-03-09 18:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicFuns', '0004_auto_20220310_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminders',
            name='remindTimeStamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 0, 16, 16, 519298)),
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicineName', models.CharField(max_length=100)),
                ('medicineDosage', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicFuns.Patient')),
            ],
        ),
    ]