# Generated by Django 2.2.5 on 2019-12-11 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 15, 31, 35, 217865)),
        ),
    ]
