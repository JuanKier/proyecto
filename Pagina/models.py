from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nombre_usuario = models.CharField(max_length = 10, unique = True)
    password_usuario = models.CharField(max_length = 10)
    nombre_completo_usuario = models.CharField(max_length = 200)