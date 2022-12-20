from rest_framework import serializers
from api.views import Producto, Cliente, Vendedor,VentasRealizadas

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"


class VentasSerializer(serializers.ModelSerializer):

    cliente = ClienteSerializer(read_only=False,many=False)
    
    class Meta:
        model = VentasRealizadas
        fields = ['producto', 'cantidad', 'cliente', 'vendedor']

    def create(self, validated_data):
        cliente = validated_data.pop('cliente')
        cliente = Cliente.objects.create(**cliente)
        venta = VentasRealizadas.objects.create(cliente=cliente,**validated_data)
        return venta

