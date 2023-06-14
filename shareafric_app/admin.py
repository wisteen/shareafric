from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *
from django import forms

# # Register your models here.
# class MultipleSelectFormField(forms.MultipleChoiceField):
#     widget = forms.SelectMultiple

# class MyModelAdminForm(forms.ModelForm):
#     elearning_interest = MultipleSelectFormField(choices=INTEREST_CHOICES)

#     class Meta:
#         model = ElearningRegistration
#         fields = '__all__'

# class MyModelAdmin(admin.ModelAdmin):
#     form = MyModelAdminForm

class IndividualRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','country_of_origin')
    list_filter = ('name', 'email','phone', 'country_of_origin', 'state_region' )
    search_fields = ('name', 'email', 'phone', 'country_of_origin', 'state_region', 'sector')

admin.site.register(IndividualRegistration, IndividualRegistrationAdmin)
admin.site.register(SMERegistration)
admin.site.register(CorporateRegistration)
admin.site.register(MentorRegistration)
admin.site.register(ElearningRegistration)
admin.site.register(ElearningAreaOfStudy)
# admin.site.register(ElearningInterest)
# admin.site.register(ElearningContactOption)
admin.site.register(TouristRegistration)
# admin.site.register(TouristInterest)
# admin.site.register(SectorOfInterest)
admin.site.register(Feedback)
admin.site.register(Webdata)
admin.site.register(theTeam)





AdminSite.index_title = 'Shareafric Admin'  # Replace with your desired index title
AdminSite.site_title = 'Shareafric Dashboard'  # Replace with your desired site title