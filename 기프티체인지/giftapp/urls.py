from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("home/", views.home),
    path("selecttheme/", views.selecttheme),
    path("selectimage/", views.selectimage),
    path("product/", views.product),
]
