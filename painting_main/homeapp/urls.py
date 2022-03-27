
from django.urls import path

from . import views

app_name="homeapp"

urlpatterns = [
    path('', views.home,name="homepage"), 
    path('about/', views.about,name="aboutpage"),
    path('our_works/', views.works,name="workpage"),
    path('service/', views.services,name="servicepage"),
    path('contact/', views.contact,name="contactpage"),
    path('services/<int:pk>/', views.services_details, name="services_details")
]