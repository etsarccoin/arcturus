# Generated by Django 2.2.5 on 2019-10-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_whychooseuscms'),
    ]

    operations = [
        migrations.CreateModel(
            name='DEVELOPMENTROADMAPCMS',
            fields=[
                ('road_map_uni_key', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('Heading1EditMonth', models.TextField()),
                ('Heading1EditLabel', models.TextField()),
                ('Heading2EditMonth', models.TextField()),
                ('Heading2EditLabel', models.TextField()),
                ('Heading3EditMonth', models.TextField()),
                ('Heading3EditLabel', models.TextField()),
                ('Heading4EditMonth', models.TextField()),
                ('Heading4EditLabel', models.TextField()),
                ('Heading5EditMonth', models.TextField()),
                ('Heading5EditLabel', models.TextField()),
                ('Heading6EditMonth', models.TextField()),
                ('Heading6EditLabel', models.TextField()),
            ],
        ),
    ]
