from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Comic

def get_comics(comic_id):
    context = {}
    if comic_id == 0:
        context['comic'] = Comic.objects.latest('pub_date')
        comic_id = context['comic'].id
    else:
        context['comic'] = get_object_or_404(Comic, id=comic_id)
        try:
            context['next'] = Comic.objects.get(id=comic_id+1)
        except Comic.DoesNotExist:
            pass

    if comic_id > 1:
        context['prev'] = Comic.objects.get(id=comic_id-1)

    return context
    

def index(request):
    context = get_comics(0)
    return render(request, "index.html", context)

def comic_page(request, id):
    context = get_comics(id)
    return render(request, 'index.html', context)

def archive(request):
    context = {"comics_list": Comic.objects.order_by('-pub_date')}
    return render(request, "archive.html", context)