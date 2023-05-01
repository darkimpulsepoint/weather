from django.urls import path

from . import views

urlpatterns = [
    path("", views.start),
    path("api/videos", views.get_videos),
]