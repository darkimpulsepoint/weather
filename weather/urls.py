from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from weather import views

urlpatterns = [
    path("", views.index),
    path("api/places", views.places),
    path("api/weather", views.weather)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)