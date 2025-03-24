from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def index(request):
    
    '''pizzas = Pizza.objects.all()
    pizzas_names_prices = [pizza.nom + " : " + str(pizza.prix) + "$" for pizza in pizzas] # récupérer le nom et le prix de chaque pizza
    pizzas_names_prices_str = ", ".join(pizzas_names_prices)
    return HttpResponse("Les Pizzas : " + pizzas_names_prices_str)'''

    return render(request, 'menu/index.html', {'pizzas': Pizza.objects.all()})