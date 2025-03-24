from django.urls import path
from . import views

app_name = 'main' # Permet de différencier les urls (namespace)

urlpatterns = [
    path('', views.index, name='index'),
]