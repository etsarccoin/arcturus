# Generated by Django 2.2.5 on 2019-10-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0009_copyrightcms'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNewsCMS',
            fields=[
                ('news_uni_key', models.SmallIntegerField(primary_key=1, serialize=False)),
                ('LatestNewsImg1', models.ImageField(upload_to='CMS/Latest News/')),
                ('LatestNewsContent1', models.TextField()),
                ('LatestNewsDate1', models.TextField()),
            ],
        ),
    ]
