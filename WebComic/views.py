import os

from django.shortcuts import render
from django.urls import reverse

def get_sorted_images():
    files = os.listdir("static/images")
    files = [os.path.join("static/images", file) for file in files]
    files.sort(key=os.path.getctime, reverse=True)
    return files

def index(request):
    files = get_sorted_images()
    new_comic = { "new_comic" : os.path.basename(files[0]) }
    return render(request, "index.html", new_comic)