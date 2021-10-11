from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length = 50, primary_key = True)
    password_usuario = models.CharField(max_length = 50)
    nombre_completo_usuario = models.CharField(max_length = 200)