
from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cons/home/',home,name='cons-home'),
    path('',mainHome,name='main-home'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('update/settings/',UpdateSettings,name='updateSetting'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),]

