# Generated by Django 2.2.5 on 2019-11-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedialcms',
            name='youtube',
            field=models.TextField(default='https://youtu.be/auC-Af16O5s'),
            preserve_default=False,
        ),
    ]
