from django.shortcuts import render
from .models import Producto

# Create your views here.

def tienda(request):

    productos=Producto.objects.all #importamos todos los productos a la variable productos


    return render(request, 'tienda/tienda.html', {'productos':productos})