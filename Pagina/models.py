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
    ci_usuario= models.CharField(max_length = 20)
    telefono_usuario= models.CharField(max_length=30)
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
    telefono_proveedor= models.CharField(max_length=30)
    direccion_proveedor=models.CharField(max_length= 200)

class Mantenimiento(models.Model):
    codigo_mant = models.AutoField(primary_key=True)
    equipo_mant = models.IntegerField(null=True)
    desc_equipo_mant = models.CharField(max_length = 200)
    horas_mant = models.IntegerField(null=True)
    actividades_mant = models.CharField(max_length = 200)
    inicio_mant = models.DateField()
    fin_mant = models.DateField()
    nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    nombre_completo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    estado_mant = models.IntegerField(default=1, null=True)

class Reparacion(models.Model):
    codigo_rep = models.AutoField(primary_key=True)
    equipo_rep = models.IntegerField(null=True)
    desc_equipo_rep = models.CharField(max_length = 200)
    horas_rep = models.IntegerField(null=True)
    actividades_rep = models.CharField(max_length = 200)
    inicio_rep = models.DateField()
    fin_rep = models.DateField()
    nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    nombre_completo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    estado_rep = models.IntegerField(default=1, null=True)

class Perifericos(models.Model):
    id_periferico=models.AutoField(primary_key=True)
    cod_periferico=models.IntegerField(null=True)
    tipo_periferico= models.IntegerField(null=True)
    marca_periferico= models.CharField(max_length=30)
    descripcion_periferico=models.CharField(max_length=200)
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    precio_compra_periferico=models.CharField(max_length=50)
    precio_venta_periferico=models.CharField(max_length=50)
    stock_periferico=models.SmallIntegerField(default=0)
    imagen_periferico = models.ImageField(upload_to="perifericos", null=True)