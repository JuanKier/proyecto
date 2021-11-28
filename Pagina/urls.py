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
    path('verusuario', views.verusuario, name='verusuario'),
    path('modusuario/<int:usu_actual>', views.modusuario, name='modusuario'),
    path('borusuario/<int:usu_actual>', views.borusuario, name='borusuario'),
    path('proveedor', views.proveedor, name='proveedor'),
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