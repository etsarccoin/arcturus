# Generated by Django 2.2.5 on 2019-12-12 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_auto_20191211_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinrequest',
            name='withdraw_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 12, 17, 4, 9, 601035)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 12, 17, 2, 5, 265008)),
        ),
    ]
