# Generated by Django 2.2.5 on 2019-10-31 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_coinrequest_reject'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileImage',
            fields=[
                ('user_mail', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('UImg', models.ImageField(upload_to='User Profile Image/')),
            ],
        ),
    ]