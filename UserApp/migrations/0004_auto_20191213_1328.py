# Generated by Django 2.2.5 on 2019-12-13 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_auto_20191212_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 13, 28, 40, 17997)),
        ),
    ]