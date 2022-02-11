# Generated by Django 3.2.6 on 2022-02-04 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id_ram', models.AutoField(primary_key=True, serialize=False)),
                ('cod_ram', models.IntegerField(null=True)),
                ('marca_ram', models.CharField(max_length=30)),
                ('descripcion_ram', models.CharField(max_length=200)),
                ('precio_compra_ram', models.IntegerField()),
                ('precio_venta_ram', models.IntegerField()),
                ('stock_ram', models.IntegerField(default=0)),
                ('imagen_ram', models.ImageField(null=True, upload_to='ram')),
                ('nombre_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
                ('tipo_ram', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.tipo_ram')),
            ],
        ),
    ]