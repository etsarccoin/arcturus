from django.contrib import admin
from .models import HomePage,common_field_update,edit_feedback,edit_hotel,edit_fooding,edit_fooding,edit_payment,\
edit_tour,edit_recreation,edit_travel,edit_about,edit_white_page,road_map_edit
# Register your models here.
admin.site.register(HomePage)
admin.site.register(common_field_update)
admin.site.register(edit_feedback)
admin.site.register(edit_hotel)
admin.site.register(edit_fooding)
admin.site.register(edit_payment)
admin.site.register(edit_tour)
admin.site.register(edit_recreation)
admin.site.register(edit_travel)
admin.site.register(edit_about)
admin.site.register(edit_white_page)
admin.site.register(road_map_edit)