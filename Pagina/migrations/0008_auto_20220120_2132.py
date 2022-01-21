# Generated by Django 3.2.6 on 2022-01-21 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0007_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ci_usuario',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion_usuario',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono_usuario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion_cliente',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion_proveedor',
            field=models.CharField(max_length=200),
        ),
    ]
