from django.urls import path
from . import views



urlpatterns = [
    
    path('profile', views.profile, name='user_auth_profile'),
]