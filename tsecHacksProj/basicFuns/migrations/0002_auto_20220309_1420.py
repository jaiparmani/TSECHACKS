# Generated by Django 3.0.6 on 2022-03-09 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicFuns', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patiendID',
            new_name='patientID',
        ),
    ]
