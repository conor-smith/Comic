from django.urls import path

from . import views

app_name = "WebComic"
urlpatterns = [
    path("", views.index, name="index"),
    path("comic/<int:id>", views.comic_page, name="comic_page"),
    path("archive", views.archive, name="archive")
]