# Generated by Django 2.2.5 on 2019-10-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_banner_heading', models.TextField(blank=True, default='Banner Heading', max_length=32)),
                ('top_banner_content', models.TextField(blank=True, default='Banner Content', max_length=128)),
                ('our_services', models.TextField(blank=True, default='our services here', max_length=1024)),
                ('services_image_1', models.ImageField(blank=True, upload_to='AdminApp/homepage/service/')),
                ('services_image_2', models.ImageField(blank=True, upload_to='AdminApp/homepage/service/')),
                ('services_image_3', models.ImageField(blank=True, upload_to='AdminApp/homepage/service/')),
                ('services_image_4', models.ImageField(blank=True, upload_to='AdminApp/homepage/service/')),
                ('services_image_5', models.ImageField(blank=True, upload_to='AdminApp/homepage/service/')),
                ('services_image_6', models.ImageField(blank=True, upload_to='AdminApp/homepage/service/')),
                ('calculate_live_cryptocurrency_content', models.TextField(blank=True, default='description of live cryptocurrency calculator', max_length=512)),
                ('feedback_background_pic', models.ImageField(blank=True, upload_to='AdminApp/homepage/feedback/')),
                ('user_feedback_profilepic_1', models.ImageField(blank=True, upload_to='AdminApp/homepage/feedback/')),
                ('user_feedback_review_1', models.TextField(blank=True, max_length=512)),
                ('user_feedback_rating_1', models.PositiveSmallIntegerField(default=0)),
                ('user_feedback_profile_pic_2', models.ImageField(blank=True, upload_to='AdminApp/homepage/feedback/')),
                ('user_feedback_review_2', models.TextField(blank=True, max_length=512)),
                ('user_feedback_rating_2', models.PositiveSmallIntegerField(default=0)),
                ('about_us_content', models.TextField(blank=True, default='description of about us', max_length=2048)),
                ('about_cryptocurrency', models.ImageField(blank=True, upload_to='AdminApp/homepage/about_crypto/')),
                ('why_choose_us_content', models.TextField(blank=True, default='reason to choose us', max_length=2048)),
                ('why_choose_us_pic', models.ImageField(blank=True, upload_to='AdminApp/homepage/why_choose_us/')),
                ('choose_us_point_1', models.CharField(blank=True, max_length=32, verbose_name='EXPERT TEAM')),
                ('choose_us_point_2', models.CharField(blank=True, max_length=32, verbose_name='FAST SERVICE')),
                ('choose_us_point_3', models.CharField(blank=True, max_length=32, verbose_name='EASY ACCESS')),
                ('choose_us_point_4', models.CharField(blank=True, max_length=32, verbose_name='LARGE WALLET')),
                ('development_roadmap_content', models.TextField(blank=True, default='some development roadmap content', max_length=512)),
                ('development_roadmap_phase_1', models.CharField(default='Jan-Feb,2019', max_length=15)),
                ('development_roadmap_content_1', models.CharField(default='some of our roadmaps', max_length=32)),
                ('development_roadmap_phase_2', models.CharField(default='Jan-Feb,2019', max_length=15)),
                ('development_roadmap_content_2', models.CharField(default='some of our roadmaps', max_length=32)),
                ('development_roadmap_phase_3', models.CharField(default='Jan-Feb,2019', max_length=15)),
                ('development_roadmap_content_3', models.CharField(default='some of our roadmaps', max_length=32)),
                ('development_roadmap_phase_4', models.CharField(default='Jan-Feb,2019', max_length=15)),
                ('development_roadmap_content_4', models.CharField(default='some of our roadmaps', max_length=32)),
                ('development_roadmap_phase_5', models.CharField(default='Jan-Feb,2019', max_length=15)),
                ('development_roadmap_content_5', models.CharField(default='some of our roadmaps', max_length=32)),
                ('development_roadmap_phase_6', models.CharField(default='Jan-Feb,2019', max_length=15)),
                ('development_roadmap_content_6', models.CharField(default='some of our roadmaps', max_length=32)),
                ('footer_acturus_desc', models.CharField(default='some Arcturus description', max_length=256)),
                ('footer_acturus_address', models.CharField(default='Street,City,Country', max_length=64)),
                ('footer_acturus_contact', models.CharField(default='(+91) 987 654 3210', max_length=20)),
                ('footer_acturus_email', models.CharField(default='office@example.com', max_length=64)),
                ('footer_latest_news_content_1', models.CharField(default='some other news', max_length=32)),
                ('footer_latest_news_pic_1', models.ImageField(blank=True, upload_to='AdminApp/homepage/news/')),
                ('footer_latest_news_content_2', models.CharField(default='some other news', max_length=32)),
                ('footer_latest_news_pic_2', models.ImageField(blank=True, upload_to='AdminApp/homepage/news/')),
                ('footer_latest_news_content_3', models.CharField(default='some other news', max_length=32)),
                ('footer_latest_news_pic_3', models.ImageField(blank=True, upload_to='AdminApp/homepage/news/')),
            ],
        ),
    ]
