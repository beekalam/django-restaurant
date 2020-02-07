from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'reservation'
urlpatterns = [
    path('', views.reserve_table, name='reserve_table'),
]
