from django.http import request
from django.urls import path
# from .views import HomeTemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
