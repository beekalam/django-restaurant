from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'meals'
urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('<slug:slug>', views.meal_detail, name='meal_detail')
]
