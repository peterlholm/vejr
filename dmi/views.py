"dmi views"
#from pathlib import Path
from django.shortcuts import render, redirect
from django.conf import settings
from dmi.radar import gen_all_png, get_last_radar_data, convert_h5_to_png, read_h5_info
from dmi.utils import get_img_tags
# Create your views here.

def index(request):
    "Start side"
    return render(request, 'index.html')

def radar(request):
    "radar picture"
    file= settings.MEDIA_ROOT / "radar/radar1.png"
    tags = get_img_tags(file)
    #print("tags", tags)
    context = {'title': tags['Title']}
    return render(request, 'radar.html', context=context)

def radar_data(request):
    "radar data test"
    get_last_radar_data()
    return redirect('radarpicture')
    #return render(request, 'test.html')

def convert(request):
    "convert function"
    filename = settings.DATA_DIR / 'radar' / "dk.com.202211051340.500_max.h5"
    convert_h5_to_png(filename)
    return render(request, 'test.html')


def read_h5(request):
    "get information from h5 file"
    filename = settings.DATA_DIR / 'radar' / "dk.com.202211051340.500_max.h5"
    filename = list((settings.DATA_DIR / 'radar').glob('*.h5'))[0]
    read_h5_info(filename)
    return render(request, 'test.html')

def gen_png(request):
    "test function"
    folder = settings.DATA_DIR / 'radar'
    gen_all_png(folder)
