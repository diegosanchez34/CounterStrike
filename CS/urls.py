from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('randomforest', randomforest, name='randomforest'),
    path('predict/', predict_view , name='predict'),
    path('predictRF/', predictRF_view , name='predictRF'),    
]
