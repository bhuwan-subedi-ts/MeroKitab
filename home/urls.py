from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('', views.login_view, name='login_view'),
   path('signup/', views.signup_view, name='signup_view'),
]