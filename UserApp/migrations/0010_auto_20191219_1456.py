# Generated by Django 2.2.5 on 2019-12-19 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0009_auto_20191219_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinrequest',
            name='trnsferin',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 14, 56, 31, 976175)),
        ),
    ]
