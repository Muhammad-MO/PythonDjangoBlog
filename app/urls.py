from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/<slug:slug>', views.post_page, name='post_page'),
    path('', views.index, name="index"),


]
