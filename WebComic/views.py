from django.shortcuts import render
from django.urls import reverse

def test_page(request):
    return render(request, "WebComic/test_page.html")