# Generated by Django 2.2.5 on 2019-12-05 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0019_auto_20191205_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinrequest',
            name='withdraw',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 5, 12, 53, 20, 204534)),
        ),
    ]
