from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('process/farm', views.farm),
    path('process/cave', views.cave),
    path('process/house', views.house),
    path('process/casino', views.casino),
    path('reset', views.reset)
]