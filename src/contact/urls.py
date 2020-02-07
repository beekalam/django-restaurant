from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.send_email, name='send_email'),
    path('success/', views.send_success, name='send_success')
]
