from django.urls import path
from Pagina import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.login, name='login'),
    path('salir', views.salir, name='salir'),
    path('profile', views.profile, name='profile'),
    path('products', views.products, name='products'),
    path('clients', views.clients, name='clients'),
    path('users', views.users, name='users')
]