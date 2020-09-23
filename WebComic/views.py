from django.shortcuts import render
from django.urls import reverse
from .models import Comic

def index(request):
    most_recent_comic = Comic.objects.order_by('-pub_date')[:1][0]
    context = { 'comic': most_recent_comic }
    return render(request, "index.html", context)