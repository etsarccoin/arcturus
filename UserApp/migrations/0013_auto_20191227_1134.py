# Generated by Django 2.2.5 on 2019-12-27 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0012_auto_20191224_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 11, 34, 18, 954414)),
        ),
    ]
