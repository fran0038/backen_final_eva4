from django.contrib import admin
from django.urls import path
from api import views as apiv
from web import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("clientev/", apiv.ClienteView.as_view()),
    path("cliented/<int:pk>", apiv.ClienteDetail.as_view()),
    path("productov/", apiv.ProductoView.as_view()),
    path("productod/<int:pk>", apiv.ProductoDetail.as_view()),
    path("vendedorv/", apiv.VendedorView.as_view()),
    path("vendedord/<int:pk>", apiv.VendedorDetail.as_view()),
    path("ventasv/", apiv.VentasViews.as_view()),
    path("ventasd/<int:pk>", apiv.VentasDetail.as_view()),
    
    path("main/", v.index, name="index"),
    path("tablaCliente/" , v.cliente, name="cliente"),
    path("ventasRealizadas/", v.ventas, name="ventas"),
    path("vendedores/", v.vendedor, name="vendedor"),

]
