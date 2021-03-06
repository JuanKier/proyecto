# Generated by Django 3.2.8 on 2022-02-21 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0004_auto_20220221_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='factura_venta',
            fields=[
                ('id_factura_venta', models.AutoField(primary_key=True, serialize=False)),
                ('nro_factura_venta', models.IntegerField()),
                ('fch_factura_venta', models.DateField(null=True)),
                ('condicion_factura_venta', models.IntegerField()),
                ('total_factura_venta', models.FloatField()),
                ('iva10_factura_venta', models.FloatField()),
                ('codigo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='timbrado_venta',
            fields=[
                ('nro_timbrado_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('fch_vencimiento_timbrado_venta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='talonario_ventas',
            fields=[
                ('id_talonario_venta', models.AutoField(primary_key=True, serialize=False)),
                ('nro_inicio_factura_venta', models.IntegerField()),
                ('nro_actual_factura_venta', models.IntegerField()),
                ('nro_fin_factura_venta', models.IntegerField()),
                ('nro_timbrado_venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.timbrado_venta')),
            ],
        ),
        migrations.CreateModel(
            name='factura_venta_detalle',
            fields=[
                ('id_factura_venta_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('cant_periferico', models.IntegerField()),
                ('subtotal_factura_venta', models.FloatField()),
                ('id_factura_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.factura_venta')),
                ('id_periferico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.perifericos')),
            ],
        ),
        migrations.AddField(
            model_name='factura_venta',
            name='nro_timbrado_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.timbrado_venta'),
        ),
    ]
