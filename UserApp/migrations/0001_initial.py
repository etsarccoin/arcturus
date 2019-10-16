# Generated by Django 2.2.5 on 2019-10-16 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminWhitePaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('white_pdf', models.FileField(upload_to='WhitePaperFolder')),
            ],
        ),
        migrations.CreateModel(
            name='CoinPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_in_usd', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CoinPriceChangeHistory',
            fields=[
                ('unique_id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('current_value', models.FloatField()),
                ('previous_value', models.FloatField()),
                ('changed_date', models.DateTimeField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoinRequest',
            fields=[
                ('unique_id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('user_mail', models.EmailField(max_length=254)),
                ('coin_price', models.FloatField()),
                ('no_coin', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('approved', models.BooleanField()),
                ('req_date', models.DateTimeField()),
                ('approved_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerifyCodes',
            fields=[
                ('user_email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('user_src_code', models.CharField(max_length=70, unique=True)),
                ('code', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ForgetPasswordTable',
            fields=[
                ('user_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionTable',
            fields=[
                ('unique_id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('req_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAccountCoin',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('no_of_coin', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCredintials',
            fields=[
                ('user_id', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedbackTable',
            fields=[
                ('user_name', models.CharField(max_length=30)),
                ('user_mail', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('user_ph', models.BigIntegerField()),
                ('overall_rating', models.SmallIntegerField()),
                ('timely_response', models.SmallIntegerField()),
                ('our_support', models.SmallIntegerField()),
                ('satisfaction_level', models.SmallIntegerField()),
                ('customer_service', models.SmallIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UsersDetail',
            fields=[
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('active_user', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserWalletTableHistory',
            fields=[
                ('unique_id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('number_coin_brought', models.FloatField()),
                ('buy_date', models.DateTimeField()),
                ('coin_price', models.FloatField()),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserWalletTable',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('wallet_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.UserWalletTableHistory')),
            ],
        ),
    ]
