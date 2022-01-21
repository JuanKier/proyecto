from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nombre_usuario = models.CharField(max_length = 10, unique = True)
    password_usuario = models.CharField(max_length = 10)
    nombre_completo_usuario = models.CharField(max_length = 200)
    tipo_usuario = models.IntegerField(null=True)
    ci_usuario= models.CharField(max_length = 50)
    telefono_usuario= models.IntegerField()
    direccion_usuario=models.CharField(max_length=200)

class Cliente(models.Model):
    codigo_cliente=models.AutoField(primary_key=True)
    nombre_cliente= models.CharField(max_length = 50)
    ruc_cliente= models.CharField(max_length = 50)
    telefono_cliente= models.IntegerField()
    direccion_cliente=models.CharField(max_length=200)
    genero_cliente=models.IntegerField(null=True)

class Proveedor(models.Model):
    codigo_proveedor=models.AutoField(primary_key=True)
    nombre_proveedor= models.CharField(max_length = 50)
    razon_social_proveedor= models.CharField(max_length = 50)
    ruc_proveedor= models.CharField(max_length = 50)
    telefono_proveedor= models.IntegerField()
    direccion_proveedor=models.CharField(max_length= 200)
    