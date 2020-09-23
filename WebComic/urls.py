from django.urls import path

from . import views

app_name = "WebComic"
urlpatterns = [
    path("", views.index, name="index")
]