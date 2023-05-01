from django.urls import path

from . import views
urlpatterns = [
    path("<str:app_name>/js", views.view_js_for_app)
]