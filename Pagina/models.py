from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Departamento(models.Model):
    codigo_departamento = models.AutoField(primary_key = True)
    nombre_departamento = models.CharField(max_length = 100)

class Ciudad(models.Model):
    codigo_ciudad = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE, null = True)

class Nacionalidad(models.Model):
    codigo_nacionalidad = models.AutoField(primary_key=True)
    descripcion_nacionalidad = models.CharField(max_length=50)

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
    telefono_cliente= models.CharField(max_length=30)
    direccion_cliente=models.CharField(max_length=200)
    genero_cliente=models.IntegerField(null=True)
    nombre_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    nombre_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)
    descripcion_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, null=True)

class Proveedor(models.Model):
    codigo_proveedor=models.AutoField(primary_key=True)
    nombre_proveedor= models.CharField(max_length = 50)
    razon_social_proveedor= models.CharField(max_length = 50)
    ruc_proveedor= models.CharField(max_length = 50)
    telefono_proveedor= models.IntegerField()
    direccion_proveedor=models.CharField(max_length= 200)


    