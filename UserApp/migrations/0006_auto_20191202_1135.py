# Generated by Django 2.2.5 on 2019-12-02 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0005_auto_20191202_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinrequest',
            name='request_type',
            field=models.CharField(default='money', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 11, 35, 27, 768818)),
        ),
    ]
