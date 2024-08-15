from django.urls import path
from . import views

urlpatterns = [
    # parses url to check if the next element/ is present
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]