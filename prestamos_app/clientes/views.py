from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente

def clientes_por_interes(request, interes):
    clientes = Cliente.objects.filter(interes=interes)

    return render(request, 'clientes/lista.html', {
        'clientes': clientes,
        'interes': interes
    })


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.grupo = request.POST.get('grupo')
        cliente.capital = request.POST.get('capital')
        cliente.save()
        return redirect('clientes_por_interes', interes=cliente.interes)

    return render(request, 'clientes/detalle.html', {'cliente': cliente})