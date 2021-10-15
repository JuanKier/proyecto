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
    path('modusuario/<int:usu_actual>', views.modusuario, name='modusuario'),
    path('borusuario/<int:usu_actual>', views.borusuario, name='borusuario')
]