from msilib.schema import Class
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


#--=========================================SERVICIOS========================================--

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


#----------------------------------------COMPATIBILIDAD-------------------------------------------

class Tipo_Ram(models.Model):
    id_tipo_ram=models.AutoField(primary_key=True)
    desc_tipo_ram=models.CharField(max_length=20)

class Tipo_Cpu(models.Model):
    id_tipo_cpu=models.AutoField(primary_key=True)
    desc_tipo_cpu=models.CharField(max_length=20)

class Tipo_Gabinete(models.Model):
    id_tipo_gabinete=models.AutoField(primary_key=True)
    desc_tipo_gabinete=models.CharField(max_length=20, null=True)

#--=========================================PRODUCTOS========================================--

class Perifericos(models.Model):
    id_periferico=models.AutoField(primary_key=True)
    cod_periferico=models.IntegerField(null=True)
    tipo_periferico= models.IntegerField(null=True)
    marca_periferico= models.CharField(max_length=30)
    descripcion_periferico=models.CharField(max_length=200)
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    precio_compra_periferico=models.IntegerField()
    precio_venta_periferico=models.IntegerField()
    stock_periferico=models.IntegerField(default=0)
    imagen_periferico = models.ImageField(upload_to="perifericos", null=True)

class Repuestos(models.Model):
    id_repuesto=models.AutoField(primary_key=True)
    cod_repuesto=models.IntegerField(null=True)
    tipo_repuesto= models.IntegerField(null=True)
    marca_repuesto= models.CharField(max_length=30)
    descripcion_repuesto=models.CharField(max_length=200)
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    precio_compra_repuesto=models.IntegerField()
    precio_venta_repuesto=models.IntegerField()
    stock_repuesto=models.IntegerField(default=0)
    imagen_repuesto = models.ImageField(upload_to="repuestos", null=True)

class RAM(models.Model):
    id_ram = models.AutoField(primary_key=True)
    cod_ram = models.IntegerField(null=True)
    tipo_ram = models.ForeignKey(Tipo_Ram, on_delete=models.CASCADE, null=True)
    marca_ram= models.CharField(max_length=30)
    descripcion_ram=models.CharField(max_length=200)
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    precio_compra_ram=models.IntegerField()
    precio_venta_ram=models.IntegerField()
    stock_ram=models.IntegerField(default=0)
    imagen_ram = models.ImageField(upload_to="ram", null=True)

class CPU(models.Model):
    id_cpu = models.AutoField(primary_key=True)
    cod_cpu = models.IntegerField(null=True)
    tipo_cpu = models.ForeignKey(Tipo_Cpu, on_delete=models.CASCADE, null=True)
    marca_cpu= models.CharField(max_length=30)
    descripcion_cpu=models.CharField(max_length=200)
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    precio_compra_cpu=models.IntegerField()
    precio_venta_cpu=models.IntegerField()
    stock_cpu=models.IntegerField(default=0)
    imagen_cpu = models.ImageField(upload_to="cpu", null=True)

class Gabinete(models.Model):
    id_gab = models.AutoField(primary_key=True)
    cod_gab = models.IntegerField(null=True)
    tipo_gabinete = models.ForeignKey(Tipo_Gabinete, on_delete=models.CASCADE, null=True)
    marca_gab= models.CharField(max_length=30)
    descripcion_gab=models.CharField(max_length=200)
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    precio_compra_gab=models.IntegerField()
    precio_venta_gab=models.IntegerField()
    stock_gab=models.IntegerField(default=0)
    imagen_gab = models.ImageField(upload_to="gab", null=True)

class Placa_base(models.Model):
    id_placa_base = models.AutoField(primary_key=True)
    cod_placa_base = models.IntegerField(null=True)
    marca_placa_base= models.CharField(max_length=30)
    descripcion_placa_base=models.CharField(max_length=200)
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    precio_compra_placa_base=models.IntegerField()
    precio_venta_placa_base=models.IntegerField()
    stock_placa_base=models.IntegerField(default=0)
    imagen_placa_base = models.ImageField(upload_to="placa_base", null=True)
    tipo_ram_placa_base = models.ForeignKey(Tipo_Ram, on_delete=models.CASCADE, null=True)
    tipo_cpu_placa_base = models.ForeignKey(Tipo_Cpu, on_delete=models.CASCADE, null=True)
    tipo_gabinete_placa_base = models.ForeignKey(Tipo_Gabinete, on_delete=models.CASCADE, null=True)

class Montaje(models.Model):
    codigo_montaje = models.AutoField(primary_key=True)
    id_placa_base = models.ForeignKey(Placa_base, on_delete=models.CASCADE, null=True)
    tipo_ram = models.ForeignKey(RAM, on_delete=models.CASCADE, null=True)
    tipo_cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, null=True)
    tipo_gabinete = models.ForeignKey(Gabinete, on_delete=models.CASCADE, null=True)
    tipo_placa_video = models.IntegerField(null=True)
    tipo_fuente = models.IntegerField(null=True)
    tipo_almacenamiento = models.IntegerField(null=True)
    id_periferico = models.ForeignKey(Perifericos, on_delete=models.CASCADE, null=True)
    horas_mont = models.IntegerField(null=True)
    actividades_mont = models.CharField(max_length = 200)
    inicio_mont = models.DateField()
    fin_mont = models.DateField()
    nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    nombre_completo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    estado_mont = models.IntegerField(default=1, null=True)




class timbrado(models.Model):
    nro_timbrado = models.IntegerField(primary_key=True)
    codigo_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fch_vencimiento_timbrado = models.DateField()

class factura_compra(models.Model):
    id_factura_compra = models.AutoField(primary_key=True)
    codigo_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nro_timbrado = models.ForeignKey(timbrado, on_delete=models.CASCADE)
    nro_factura_compra = models.IntegerField()
    fch_factura_compra = models.DateField()
    condicion_factura_compra = models.IntegerField()
    iva10_factura_compra = models.FloatField()
    total_factura_compra = models.FloatField()

class factura_compra_detalle(models.Model):
    id_factura_compra_detalle = models.AutoField(primary_key=True)
    id_factura_compra = models.ForeignKey(factura_compra, on_delete=models.CASCADE)
    id_periferico = models.ForeignKey(Perifericos, on_delete=models.CASCADE)
    cant_periferico = models.IntegerField()
    subtotal_periferico = models.FloatField()


class timbrado_venta(models.Model):
    nro_timbrado_venta = models.IntegerField(primary_key=True)
    fch_vencimiento_timbrado_venta = models.DateField()

class talonario_ventas(models.Model):
    id_talonario_venta = models.AutoField(primary_key=True)
    nro_timbrado_venta = models.ForeignKey(timbrado_venta, on_delete=models.CASCADE, null=True)
    nro_inicio_factura_venta = models.IntegerField()
    nro_actual_factura_venta = models.IntegerField()
    nro_fin_factura_venta = models.IntegerField()

class factura_venta(models.Model):
    id_factura_venta = models.AutoField(primary_key=True)
    codigo_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nro_timbrado_venta = models.ForeignKey(timbrado_venta, on_delete=models.CASCADE)
    nro_factura_venta = models.IntegerField()
    fch_factura_venta = models.DateField(null=True)
    condicion_factura_venta = models.IntegerField()
    total_factura_venta = models.FloatField()
    iva10_factura_venta = models.FloatField()

class factura_venta_detalle(models.Model):
    id_factura_venta_detalle = models.AutoField(primary_key=True)
    id_factura_venta = models.ForeignKey(factura_venta, on_delete=models.CASCADE)
    id_periferico = models.ForeignKey(Perifericos, on_delete=models.CASCADE)
    cant_periferico = models.IntegerField()
    subtotal_factura_venta = models.FloatField()