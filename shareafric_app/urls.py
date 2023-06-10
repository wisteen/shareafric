from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shareafric_app'

urlpatterns = [
    # Add your URL patterns here
    path('', views.home, name='home'),
    path('submit_form', views.submit_form, name='submit_form'),
    path('sme_form', views.sme_form, name='sme_form'),
    path('corporate_form', views.corporate_form, name='corporate_form'),
    path('mentor_form', views.mentor_form, name='mentor_form'),
    path('elearning_form', views.elearning_form, name='elearning_form'),
    path('tourist', views.tourist, name='tourist'),
    

    # other paths...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
