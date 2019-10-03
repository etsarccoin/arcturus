from django import forms

from .models import HomePage
class HomePageEditForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = '__all__'
        widgets = {
           "top_banner_heading": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "top_banner_content": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "our_services": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            #"services_image_1": forms. ,
            #"services_image_2": forms. ,
            #"services_image_3": forms. ,
            #"services_image_4": forms. ,
            #"services_image_5": forms. ,
            #"services_image_6": forms. ,
           "calculate_live_cryptocurrency_content": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            #"feedback_background_pic": forms. ,
            #"user_feedback_profilepic_1": forms. ,
           "user_feedback_review_1": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            #"user_feedback_rating_1": forms. ,
            #"user_feedback_profile_pic_2": forms. ,
            "user_feedback_review_2": forms.TextInput(attrs={'class':'form-control form-control-sm'})  ,
            #"user_feedback_rating_2": forms. ,
           "about_us_content": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "about_cryptocurrency": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "about_cryptocurrency": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "why_choose_us_content": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            #"why_choose_us_pic": forms. ,
            #"choose_us_point_1": forms. ,
            #"choose_us_point_2": forms. ,
            #"choose_us_point_3": forms. ,
            #"choose_us_point_4": forms. ,
           "development_roadmap_content": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_phase_1": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_content_1": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_phase_2": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_content_2": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_phase_3": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_content_3": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_phase_4": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_content_4": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_phase_5": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_content_5": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_phase_6": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "development_roadmap_content_6": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,

           "footer_acturus_desc": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "footer_acturus_address": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "footer_acturus_contact": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
           "footer_acturus_email": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,

           "footer_latest_news_content_1": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            #"footer_latest_news_pic_1": forms. ,
           "footer_latest_news_content_2": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            #"footer_latest_news_pic_2": forms. ,
           "footer_latest_news_content_3": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            #"footer_latest_news_pic_3": forms. ,
            
            }
        
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # self.fields.widget.attrs.update({'class': 'form-control form-control-sm'})
        # self.fields['comment'].widget.attrs.update(size='40')