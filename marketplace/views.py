from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from .models import Producto


@login_required
def home(request):
    productos = Producto.objects.all()
    query = request.GET.get('q', '')
    
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query) |
            Q(tipo__icontains=query)
        )
    
    context = {
        'productos': productos,
        'query': query
    }
    return render(request, 'marketplace/home.html', context)
