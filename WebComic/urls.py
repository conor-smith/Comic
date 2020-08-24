from django.urls import path

from . import views

app_name = "WebComic"
urlpatterns = [
    path("", views.test_page, name="test_page")
]