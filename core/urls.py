from django.urls import path
from .views import load, home

app_name = 'core'
urlpatterns = [
    path('load/', load, name='load'),
    path('', home, name='home')
]