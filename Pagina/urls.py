from django.urls import path
from Pagina import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.login, name='login'),
    path('salir', views.salir, name='salir'),
    path('produccion', views.produccion, name='produccion'),

    path('verusuario', views.verusuario, name='verusuario'),
    path('modusuario/<int:usu_actual>', views.modusuario, name='modusuario'),
    path('borusuario/<int:usu_actual>', views.borusuario, name='borusuario'),
    
    path('vercliente', views.vercliente, name='vercliente'),
    path('modcliente/<int:cliente_actual>', views.modcliente, name='modcliente'),
    path('borcliente/<int:cliente_actual>', views.borcliente, name='borcliente'),

    path('verproveedor', views.verproveedor, name='verproveedor'),
    path('modproveedor/<int:proveedor_actual>', views.modproveedor, name='modproveedor'),
    path('borproveedor/<int:proveedor_actual>', views.borproveedor, name='borproveedor'),

    # ----------------------------------------MAINTENACE---------------------------------------------------
    
      #--Departamentos
    path('verdepartamento', views.verdepartamento, name='verdepartamento'),
    path('moddepartamento/<int:departamento_actual>', views.moddepartamento, name='moddepartamento'),
    path('bordepartamento/<int:departamento_actual>', views.bordepartamento, name='bordepartamento'),

        #--Ciudades
    path('verciudad', views.verciudad, name='verciudad'),
    path('modciudad/<int:ciudad_actual>', views.modciudad, name='modciudad'),
    path('borciudad/<int:ciudad_actual>', views.borciudad, name='borciudad'),
        
        #--Nacionalidades
    path('vernacionalidad', views.vernacionalidad, name='vernacionalidad'),
    path('modnacionalidad/<int:nacionalidad_actual>', views.modnacionalidad, name='modnacionalidad'),
    path('bornacionalidad/<int:nacionalidad_actual>', views.bornacionalidad, name='bornacionalidad'),

        #--Tipos_de_Ram
    path('vertipo_ram', views.vertipo_ram, name='vertipo_ram'),
    path('modtipo_ram/<int:tipo_ram_actual>', views.modtipo_ram, name='modtipo_ram'),
    path('bortipo_ram/<int:tipo_ram_actual>', views.bortipo_ram, name='bortipo_ram'),

        #--Tipos_de_Cpu
    path('vertipo_cpu', views.vertipo_cpu, name='vertipo_cpu'),
    path('modtipo_cpu/<int:tipo_cpu_actual>', views.modtipo_cpu, name='modtipo_cpu'),
    path('bortipo_cpu/<int:tipo_cpu_actual>', views.bortipo_cpu, name='bortipo_cpu'),

        #--Tipos_de_Gabinete
    path('vertipo_gabinete', views.vertipo_gabinete, name='vertipo_gabinete'),
    path('modtipo_gabinete/<int:tipo_gabinete_actual>', views.modtipo_gabinete, name='modtipo_gabinete'),
    path('bortipo_gabinete/<int:tipo_gabinete_actual>', views.bortipo_gabinete, name='bortipo_gabinete'),

# ----------------------------------------PRODUCCION---------------------------------------------------
    
    #--Mantenimiento
    path('vermant', views.vermant, name='vermant'),
    path('modmant/<int:mant_actual>', views.modmant, name='modmant'),
    path('bormant/<int:mant_actual>', views.bormant, name='bormant'),

     #--Reparación
    path('verrep', views.verrep, name='verrep'),
    path('modrep/<int:rep_actual>', views.modrep, name='modrep'),
    path('borrep/<int:rep_actual>', views.borrep, name='borrep'),

     #--Montaje
    path('vermontaje', views.vermontaje, name='vermontaje'),
    path('nuevomontaje/<int:placa_base_actual>/<int:montaje_actual>', views.nuevomontaje, name='nuevomontaje'),
    path('bormontaje/<int:montaje_actual>', views.bormontaje, name='bormontaje'),
    

# ----------------------------------------PRODUCTOS---------------------------------------------------

    #--Perifericos
    path('perifericover', views.perifericover, name='perifericover'),
    path('perifericomod/<int:periferico_actual>', views.perifericomod, name='perifericomod'),
    path('perifericobor/<int:periferico_actual>', views.perifericobor, name='perifericobor'),

    #--Repuestos
    path('repuestover', views.repuestover, name='repuestover'),
    path('repuestomod/<int:repuesto_actual>', views.repuestomod, name='repuestomod'),
    path('repuestobor/<int:repuesto_actual>', views.repuestobor, name='repuestobor'),
        
    #--Placa_Base
    path('ver_placa_base', views.ver_placa_base, name='ver_placa_base'),
    path('mod_placa_base/<int:placa_base_actual>', views.mod_placa_base, name='mod_placa_base'),
    path('bor_placa_base/<int:placa_base_actual>', views.bor_placa_base, name='bor_placa_base'),

    #--RAM
    path('ver_ram', views.ver_ram, name='ver_ram'),
    path('mod_ram/<int:ram_actual>', views.mod_ram, name='mod_ram'),
    path('bor_ram/<int:ram_actual>', views.bor_ram, name='bor_ram'),

    #--CPU
    path('ver_cpu', views.ver_cpu, name='ver_cpu'),
    path('mod_cpu/<int:cpu_actual>', views.mod_cpu, name='mod_cpu'),
    path('bor_cpu/<int:cpu_actual>', views.bor_cpu, name='bor_cpu'),

    #--GABINETE
    path('ver_gab', views.ver_gab, name='ver_gab'),
    path('mod_gab/<int:gab_actual>', views.mod_gab, name='mod_gab'),
    path('bor_gab/<int:gab_actual>', views.bor_gab, name='bor_gab'),


# ----------------------------------------VENTA Y COMPRA---------------------------------------------------
    #--VENTA
    path('venta', views.venta, name='venta'),

    #--COMPRA
    path('compra', views.compra, name='compra'),
    path('compra_detalle}', views.compra_detalle, name='compra_detalle'),

    
    path('ver_productos', views.ver_productos, name='ver_productos'),
    path('inventario', views.inventario, name='inventario'),

    path('inventario', views.inventario, name='inventario'),
  
]

