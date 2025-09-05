from django.urls import path
from . import views

app_name = "readers"

urlpatterns = [
    path("", views.home, name="home"),
    path("interests", views.interests, name="interests")
]
