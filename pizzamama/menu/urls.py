from django.urls import path
from . import views

app_name = 'menu' # Permet de différencier les urls (namespace)

urlpatterns = [
    path('', views.index, name='index'),
]
