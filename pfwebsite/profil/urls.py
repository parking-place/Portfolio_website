from django.contrib import admin
from django.urls import path, include
# from .veiws import *
from . import views

urlpatterns = [
    path("", views.Profil.as_view(), name="profile"),
]