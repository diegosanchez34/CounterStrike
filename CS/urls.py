from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

from CS import views

urlpatterns = [
    path('', views.index, name='index'),
] 