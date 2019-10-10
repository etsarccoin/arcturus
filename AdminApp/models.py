from django.db import models

<<<<<<< HEAD

class HomePage(models.Model):
    top_banner_heading = models.TextField(default = "Banner Heading",max_length = 32,blank = True)
    top_banner_content = models.TextField(default = "Banner Content",max_length = 128, blank = True)
    our_services = models.TextField(default = "our services here",max_length = 1024,blank = True)
    services_image_1 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_image_2 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_image_3 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_image_4 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_image_5 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_image_6 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    calculate_live_cryptocurrency_content = models.TextField(default="description of live cryptocurrency calculator",max_length=512,blank=True)
    feedback_background_pic = models.ImageField(upload_to = "AdminApp/homepage/feedback/",blank=True)
    user_feedback_profilepic_1 = models.ImageField(upload_to="AdminApp/homepage/feedback/",blank=True)
    user_feedback_review_1 = models.TextField(blank=True,max_length=512)
    user_feedback_rating_1 = models.PositiveSmallIntegerField(default=0)
    user_feedback_profile_pic_2 = models.ImageField(upload_to="AdminApp/homepage/feedback/",blank=True)
    user_feedback_review_2 = models.TextField(blank=True,max_length=512)
    user_feedback_rating_2 = models.PositiveSmallIntegerField(default=0)
    about_us_content = models.TextField(max_length=2048,blank=True, default="description of about us")
    about_cryptocurrency = models.TextField(max_length=5000,blank=True,default="about cryptocurrency")
    about_cryptocurrency = models.ImageField(upload_to="AdminApp/homepage/about_crypto/",blank=True)
    why_choose_us_content = models.TextField(max_length=2048,blank=True,default="reason to choose us")
    why_choose_us_pic = models.ImageField(upload_to="AdminApp/homepage/why_choose_us/",blank=True)
    choose_us_point_1 = models.CharField("EXPERT TEAM",max_length=32,blank=True)
    choose_us_point_2 = models.CharField("FAST SERVICE",max_length=32,blank=True)
    choose_us_point_3 = models.CharField("EASY ACCESS",max_length=32,blank=True)     
    choose_us_point_4 = models.CharField("LARGE WALLET",max_length=32,blank=True)
    development_roadmap_content = models.TextField(default="some development roadmap content",blank=True,max_length=512)
    development_roadmap_phase_1 = models.CharField(default="Jan-Feb,2019",max_length=15)
    development_roadmap_content_1 = models.CharField(default="some of our roadmaps",max_length = 32)
    development_roadmap_phase_2 = models.CharField(default="Jan-Feb,2019",max_length=15)
    development_roadmap_content_2 = models.CharField(default="some of our roadmaps",max_length = 32)
    development_roadmap_phase_3 = models.CharField(default="Jan-Feb,2019",max_length=15)
    development_roadmap_content_3 = models.CharField(default="some of our roadmaps",max_length = 32)
    development_roadmap_phase_4 = models.CharField(default="Jan-Feb,2019",max_length=15)
    development_roadmap_content_4 = models.CharField(default="some of our roadmaps",max_length = 32)
    development_roadmap_phase_5 = models.CharField(default="Jan-Feb,2019",max_length=15)
    development_roadmap_content_5 = models.CharField(default="some of our roadmaps",max_length = 32)
    development_roadmap_phase_6 = models.CharField(default="Jan-Feb,2019",max_length=15)
    development_roadmap_content_6 = models.CharField(default="some of our roadmaps",max_length = 32)

    footer_acturus_desc = models.CharField(default="some Arcturus description",max_length=256)
    footer_acturus_address = models.CharField(default="Street,City,Country",max_length=64)
    footer_acturus_contact = models.CharField(default = "(+91) 987 654 3210",max_length=20)
    footer_acturus_email = models.CharField(default = "office@example.com",max_length=64)

    footer_latest_news_content_1 = models.CharField(default="some other news",max_length=32)
    footer_latest_news_pic_1 = models.ImageField(upload_to = "AdminApp/homepage/news/",blank=True)
    footer_latest_news_content_2 = models.CharField(default="some other news",max_length=32)
    footer_latest_news_pic_2 = models.ImageField(upload_to = "AdminApp/homepage/news/",blank=True)
    footer_latest_news_content_3 = models.CharField(default="some other news",max_length=32)
    footer_latest_news_pic_3 = models.ImageField(upload_to = "AdminApp/homepage/news/",blank=True)


    def save(self, *args, **kwargs):
        all_obj = HomePage.objects.all()
        if len(all_obj > 1):
            HomePage.objects.all().delete()

        super().save(*args, **kwargs)   
=======
class OurSerice(models.Model):
    description = models.TextField()
    updated_at = models.DateTimeField()


class SocialMedialLink(models.Model):
    facebook_link = models.TextField()
    twitter_link = models.TextField()
    googleplus = models.TextField()
    linkedin = models.TextField()

>>>>>>> 1a802fcedf47283f8cc03cc3d51fc873db10205b
