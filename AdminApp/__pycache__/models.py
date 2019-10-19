from django.db import models
class HomePage(models.Model):
    our_services = models.TextField(default = "our services here",max_length = 1024,blank = True)
    services_pic_1 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_pic_2 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_pic_3 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_pic_4 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_pic_5 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    services_pic_6 = models.ImageField(upload_to = "AdminApp/homepage/service/",blank=True)
    calculate_live_cryptocurrency_content = models.TextField(default="description of live cryptocurrency calculator",max_length=512,blank=True)
    feedback_background_pic = models.ImageField(upload_to = "AdminApp/homepage/feedback/",blank=True)
    about_us_content = models.TextField(max_length=2048,blank=True)
    about_cryptocurrency = models.TextField(max_length=5000,blank=True)
    about_cryptocurrency = models.ImageField(upload_to="AdminApp/homepage/about_crypto/",blank=True)
    why_choose_us_content = models.TextField(max_length=2048,blank=True)
    why_choose_us_pic = models.ImageField(upload_to="AdminApp/homepage/why_choose_us/",blank=True)
    choose_us_point_1 = models.CharField(max_length = 2048,blank=True)
    choose_us_point_2 = models.CharField(max_length = 2048,blank=True)
    choose_us_point_3 = models.CharField(max_length = 2048,blank=True)     
    choose_us_point_4 = models.CharField(max_length = 2048,blank=True)

    footer_acturus_desc = models.CharField(default="some Arcturus description",max_length=256)
    footer_acturus_address = models.CharField(default="Street,City,Country",max_length=64)
    footer_acturus_contact = models.CharField(default = "(+91) 987 654 3210",max_length=20)
    footer_acturus_email = models.CharField(default = "office@example.com",max_length=64)
    def save(self, *args, **kwargs):
        all_obj = HomePage.objects.all()
        if len(all_obj) > 1:
            HomePage.objects.all().delete()
        super().save(*args, **kwargs)   
        
class OurSerice(models.Model):
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    def save(self, *args, **kwargs):
        all_obj = OurSerice.objects.all()
        if len(all_obj) > 1:
            OurSerice.objects.all().delete()
        super().save(*args, **kwargs) 


class SocialMedialLink(models.Model):
    facebook_link = models.TextField(blank=True)
    twitter_link = models.TextField(blank=True)
    googleplus = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    def save(self, *args, **kwargs):
        all_obj = SocialMedialLink.objects.all()
        if len(all_obj) > 1:
            SocialMedialLink.objects.all().delete()
        super().save(*args, **kwargs) 
class common_field_update(models.Model):
    top_banner_heading=models.CharField(max_length = 2048,blank=True)
    top_banner_content=models.CharField(max_length = 2048,blank=True)
    footer_acturus_desc=models.CharField(max_length = 2048,blank=True)
    footer_acturus_address=models.CharField(max_length = 2048,blank=True)
    footer_acturus_contact=models.CharField(max_length = 2048,blank=True)
    footer_acturus_email=models.CharField(max_length = 2048,blank=True)
    footer_latest_news_content_1 = models.CharField(max_length = 2048,blank=True)
    footer_latest_news_pic_1 = models.ImageField(upload_to = "AdminApp/homepage/news/",blank=True)
    footer_latest_news_content_2 = models.CharField(max_length = 2048,blank=True)
    footer_latest_news_pic_2 = models.ImageField(upload_to = "AdminApp/homepage/news/",blank=True)
    footer_latest_news_content_3 = models.CharField(max_length = 2048,blank=True)
    footer_latest_news_pic_3 = models.ImageField(upload_to = "AdminApp/homepage/news/",blank=True)
    def save(self, *args, **kwargs):
        all_obj = common_field_update.objects.all()
        if len(all_obj) > 1:
            common_field_update.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_feedback(models.Model):
    user_feedback_review=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_feedback.objects.all()
        if len(all_obj) > 1:
            edit_feedback.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_hotel(models.Model):
    content_heading=models.CharField(max_length = 2048,blank=True)
    content_body=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_hotel.objects.all()
        if len(all_obj) > 1:
            edit_hotel.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_fooding(models.Model):
    fooding_heading=models.CharField(max_length = 2048,blank=True)
    fooding_body=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_fooding.objects.all()
        if len(all_obj) > 1:
            edit_fooding.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_payment(models.Model):
    payment_heading=models.CharField(max_length = 2048,blank=True)
    payment_body=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_payment.objects.all()
        if len(all_obj) > 1:
            edit_payment.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_tour(models.Model):
    tour_heading=models.CharField(max_length = 2048,blank=True)
    tour_body=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_tour.objects.all()
        if len(all_obj) > 1:
            edit_tour.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_recreation(models.Model):
    recreation_heading=models.CharField(max_length = 2048,blank=True)
    recreation_body=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_recreation.objects.all()
        if len(all_obj) > 1:
            edit_recreation.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_travel(models.Model):
    travel_heading=models.CharField(max_length = 2048,blank=True)
    travel_body=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_travel.objects.all()
        if len(all_obj) > 1:
            edit_travel.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_about(models.Model):
    about_heading=models.CharField(max_length = 2048,blank=True)
    about_body=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_about.objects.all()
        if len(all_obj) > 1:
            edit_about.objects.all().delete()
        super().save(*args, **kwargs) 
class edit_white_page(models.Model):
    white_page_heading=models.CharField(max_length = 2048,blank=True)
    white_page_body=models.CharField(max_length = 2048,blank=True)
    def save(self, *args, **kwargs):
        all_obj = edit_white_page.objects.all()
        if len(all_obj) > 1:
            edit_white_page.objects.all().delete()
        super().save(*args, **kwargs) 
class road_map_edit(models.Model):
    development_roadmap_content = models.TextField(blank=True)
    development_roadmap_phase_1 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_content_1 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_image_1= models.ImageField(upload_to = "AdminApp/homepage/roadmap/",blank=True)
    development_roadmap_phase_2 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_content_2 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_image_2= models.ImageField(upload_to = "AdminApp/homepage/roadmap/",blank=True)
    development_roadmap_phase_3 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_content_3 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_image_3= models.ImageField(upload_to = "AdminApp/homepage/roadmap/",blank=True)
    development_roadmap_phase_4 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_content_4 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_image_4= models.ImageField(upload_to = "AdminApp/homepage/roadmap/",blank=True)
    development_roadmap_phase_5 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_content_5 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_image_5= models.ImageField(upload_to = "AdminApp/homepage/roadmap/",blank=True)
    development_roadmap_phase_6 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_content_6 = models.CharField(max_length = 2048,blank=True)
    development_roadmap_image_6= models.ImageField(upload_to = "AdminApp/homepage/roadmap/",blank=True)
    def save(self, *args, **kwargs):
        all_obj = road_map_edit.objects.all()
        if len(all_obj) > 1:
            road_map_edit.objects.all().delete()
        super().save(*args, **kwargs) 