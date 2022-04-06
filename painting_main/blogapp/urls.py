from django.urls import path
from . import views

app_name='blogapp'

urlpatterns = [ 
    path('blog/', views.blog, name='blogpage'),
    path('blog_details/<int:pk>', views.blog_details, name='blog_details'),
]