from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index')
    path('predict/', views.predict_view , name='predict'),
    path('predictRF/', views.predictRF_view , name='predictRF'),
    
]
