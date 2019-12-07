from django import forms

from .models import HomePage,common_field_update,edit_feedback,edit_hotel,edit_fooding,edit_payment,edit_tour,edit_recreation,road_map_edit,edit_travel,edit_about,edit_white_page
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
class common_field(forms.ModelForm):
    class Meta:
      model = common_field_update
      fields = '__all__'
      widgets = {
            "top_banner_heading": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            "top_banner_content": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            "footer_acturus_desc": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            "footer_acturus_address": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            "footer_acturus_contact": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            "footer_acturus_email": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            "footer_latest_news_content_1": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            "footer_latest_news_content_2": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
            "footer_latest_news_content_3": forms.TextInput(attrs={'class':'form-control form-control-sm'}) ,
      }
class feed_back_edit(forms.ModelForm):
  class Meta:
    model = edit_feedback
    fields='__all__'
    widget={
    "user_feedback_review": forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }

class hotels_edit(forms.ModelForm):
  class Meta:
    model=edit_hotel
    fields="__all__"
    widget={
    "content_heading":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
    "content_body":forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }
class fooding_edit(forms.ModelForm):
  class Meta:
    model=edit_fooding
    fields="__all__"
    widget={
    "fooding_heading":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
    "fooding_body":forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }
class payments_edit(forms.ModelForm):
  class Meta:
    model=edit_payment
    fields="__all__"
    widget={
    "payment_heading":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
    "payment_body":forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }
class tour_edit(forms.ModelForm):
  class Meta:
    model=edit_tour
    fields="__all__"
    widget={
    "tour_heading":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
    "tour_body":forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }
class recreation_edit(forms.ModelForm):
  class Meta:
    model=edit_recreation
    fields="__all__"
    widget={
    "recreation_heading":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
    "recreation_body":forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }
class travel_edit(forms.ModelForm):
  class Meta:
    model=edit_travel
    fields="__all__"
    widget={
    "travel_heading":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
    "travel_body":forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }
  
class about_us_edit(forms.ModelForm):
  class Meta:
    model=edit_about
    fields="__all__"
    widget={
    "about_heading":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
    "about_body":forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }
class white_page_edit(forms.ModelForm):
  class Meta:
    model=edit_white_page
    fields="__all__"
    widget={
    "white_page_heading":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
    "white_page_body":forms.TextInput(attrs={'class':'form-control form-control-sm'})
    }
class edit_road_map(forms.ModelForm):
  class Meta:
    model=road_map_edit()
    fields="__all__"
    widget={
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
    }