from django.db import models
from rest_framework import serializers

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=50, null=False)
    stock = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return ( self.nombre ) 
    

class Cliente(models.Model):

    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=50)
   
   
    def __str__(self):
        return ( self.nombre +" "+ self.apellido  ) 

class Vendedor(models.Model):

    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=50)
    
    def __str__(self):
        texto = self.nombre +" "+ self.apellido 
        return texto 

class VentasRealizadas(models.Model):
    
    producto =models.ForeignKey(Producto,null=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    cliente= models.ForeignKey(Cliente,null=False, on_delete=models.CASCADE)
    vendedor= models.ForeignKey(Vendedor,null=False, on_delete=models.CASCADE)

    