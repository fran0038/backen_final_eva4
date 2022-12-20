from django.shortcuts import render
from api.models import Producto, Cliente,VentasRealizadas ,Vendedor
from api.serializers import VentasSerializer

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    data = {"listaProductos": productos}
    return render(request, "index.html", data)


def cliente(request):
    cliente = Cliente.objects.all()
    data = {'cliente': cliente}
    return render(request, 'tablaCliente.html', data)


def vendedor(request):
    vendedor = Vendedor.objects.all()
    data = {'vendedor': vendedor}

    return render(request, 'vendedores.html', data)

def ventas(request):
    ventas = VentasRealizadas.objects.all()
    data= {'ventas': ventas}

    return render(request, "ventas.html",data)
