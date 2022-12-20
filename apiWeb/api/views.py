from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api.models import *
from .serializers import *


# Create your views here.
class ProductoView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class ProductoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)



class ClienteView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class ClienteDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)



class VendedorView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class VendedorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class VentasViews(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = VentasRealizadas.objects.all()
    serializer_class = VentasSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class VentasDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = VentasRealizadas.objects.all()
    serializer_class = VentasSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
