# Generated by Django 2.2.5 on 2019-12-13 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_auto_20191213_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinrequest',
            name='withdraw_date',
        ),
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 15, 35, 19, 751544)),
        ),
    ]
