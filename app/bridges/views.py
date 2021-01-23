from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Bridge

# Create your views here.
def index(request):
    bridges = Bridge.objects.all()

    paginator = Paginator(bridges, 3) # items per page
    page = request.GET.get('page')
    paged_bridges = paginator.get_page(page)

    context = {
        'bridges': paged_bridges
    }
    return render(request, 'bridges/bridges.html', context)

def bridge(request, id):
    bridge = get_object_or_404(Bridge, pk=id)

    context = {
        'bridge' : bridge
    }

    return render(request, 'bridges/bridge.html', context)

def search(request):
    return render(request, 'bridges/search.html')
