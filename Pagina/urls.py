from django.urls import path
from Pagina import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.login, name='login'),
    path('salir', views.salir, name='salir'),
    path('profile', views.profile, name='profile'),
    path('products', views.products, name='products'),
    path('clients', views.clients, name='clients'),
    path('users', views.users, name='users'),
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
    
    path('verdepartamento', views.verdepartamento, name='verdepartamento'),
    path('moddepartamento/<int:departamento_actual>', views.moddepartamento, name='moddepartamento'),
    path('bordepartamento/<int:departamento_actual>', views.bordepartamento, name='bordepartamento'),

    path('verciudad', views.verciudad, name='verciudad'),
    path('modciudad/<int:ciudad_actual>', views.modciudad, name='modciudad'),
    path('borciudad/<int:ciudad_actual>', views.borciudad, name='borciudad'),

    path('vernacionalidad', views.vernacionalidad, name='vernacionalidad'),
    path('modnacionalidad/<int:nacionalidad_actual>', views.modnacionalidad, name='modnacionalidad'),
    path('bornacionalidad/<int:nacionalidad_actual>', views.bornacionalidad, name='bornacionalidad'),

# ----------------------------------------PRODUCCION---------------------------------------------------
    
    #--Mantenimiento
    path('vermant', views.vermant, name='vermant'),
    path('modmant/<int:mant_actual>', views.modmant, name='modmant'),
    path('bormant/<int:mant_actual>', views.bormant, name='bormant'),


    path('inventario', views.inventario, name='inventario'),

    path('cpu', views.cpu, name='cpu'),
    path('case', views.case, name='case'),
    path('motherboard', views.motherboard, name='motherboard'),
    path('perifericos', views.perifericos, name='perifericos'),
    path('psu', views.psu, name='psu'),
    path('ram', views.ram, name='ram'),
    path('stg', views.stg, name='stg'),
    path('vga', views.vga, name='vga'),    
]