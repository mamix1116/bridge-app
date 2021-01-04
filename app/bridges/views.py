from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'bridges/bridges.html')

def bridge(request):
    return render(request, 'bridges/bridge.html')

def search(request):
    return render(request, 'bridges/search.html')
