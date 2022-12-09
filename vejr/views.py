from django.shortcuts import render
from django.conf import settings
from vejr.utils import get_img_tags

def index(request):
    "Start side"
    return render(request, 'index.html')

def radar_picture(request):
    "radar picture"
    file= settings.MEDIA_ROOT / "radar/radar1.png"
    tags = get_img_tags(file)
    #print("tags", tags)
    context = {'title': tags['Title']}
    return render(request, 'radar.html', context=context)
