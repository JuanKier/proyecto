from django.urls import path
from pagina import views

urlpatterns = [
    path('', views.login, name='login'),
    path('menu', views.inicio, name='inicio'),
    path('acerca', views.acerca, name='acerca'),
    path('salir', views.salir, name='salir'),
    path('verusuario', views.verusuario, name='verusuario'),
    path('modusuario/<int:usu_actual>', views.modusuario, name='modusuario'),
    path('borusuario/<int:usu_actual>', views.borusuario, name='borusuario'),
]
