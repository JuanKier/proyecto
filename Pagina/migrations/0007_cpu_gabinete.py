# Generated by Django 3.2.6 on 2022-02-05 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0006_placa_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gabinete',
            fields=[
                ('id_gab', models.AutoField(primary_key=True, serialize=False)),
                ('cod_gab', models.IntegerField(null=True)),
                ('marca_gab', models.CharField(max_length=30)),
                ('descripcion_gab', models.CharField(max_length=200)),
                ('precio_compra_gab', models.IntegerField()),
                ('precio_venta_gab', models.IntegerField()),
                ('stock_gab', models.IntegerField(default=0)),
                ('imagen_gab', models.ImageField(null=True, upload_to='gab')),
                ('nombre_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
                ('tipo_gabinete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.tipo_gabinete')),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id_cpu', models.AutoField(primary_key=True, serialize=False)),
                ('cod_cpu', models.IntegerField(null=True)),
                ('marca_cpu', models.CharField(max_length=30)),
                ('descripcion_cpu', models.CharField(max_length=200)),
                ('precio_compra_cpu', models.IntegerField()),
                ('precio_venta_cpu', models.IntegerField()),
                ('stock_cpu', models.IntegerField(default=0)),
                ('imagen_cpu', models.ImageField(null=True, upload_to='cpu')),
                ('nombre_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
                ('tipo_cpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.tipo_cpu')),
            ],
        ),
    ]