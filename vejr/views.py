from django.shortcuts import render

# Create your views here.


def index(request):
    "Start side"
    return render(request, 'index.html')
