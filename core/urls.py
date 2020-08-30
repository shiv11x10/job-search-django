from django.urls import path
from .views import load, HomeView

app_name = 'core'
urlpatterns = [
    path('load/', load, name='load'),
    path('', HomeView.as_view(), name='base')
]