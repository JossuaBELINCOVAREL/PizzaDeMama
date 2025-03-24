from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix') # Permet de visualiser les infos des pizzas
    search_fields = ['nom']


admin.site.register(Pizza, PizzaAdmin) # Permet de voir les pizzas dans l'admin