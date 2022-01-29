from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("settings/", views.settings, name="settings"),
    path("user-settings/", views.settings, name="user-settings"),

]
