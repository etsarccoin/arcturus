# Generated by Django 2.2.5 on 2019-12-19 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0010_auto_20191219_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedbacktable',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 17, 37, 36, 454129)),
        ),
    ]
