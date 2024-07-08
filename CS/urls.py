from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('predict/', predict_view , name='predict'),
    path('predictRF/', predictRF_view , name='predictRF'),
    
]
