"urls for vejr app"
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index')
    # path('radar', views.radar,name="radarpicture"),
    # path('radardata', views.radar_data),
    # path('convert', views.convert),
    # path('readh5', views.read_h5),
    # path('gen_all_png', views.gen_png)
]
