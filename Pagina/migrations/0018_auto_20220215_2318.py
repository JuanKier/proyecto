# Generated by Django 3.2.6 on 2022-02-16 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0017_auto_20220208_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='factura_compra',
            fields=[
                ('id_factura_compra', models.AutoField(primary_key=True, serialize=False)),
                ('nro_factura_compra', models.IntegerField()),
                ('fch_factura_compra', models.DateField()),
                ('condicion_factura_compra', models.IntegerField()),
                ('iva10_factura_compra', models.FloatField()),
                ('total_factura_compra', models.FloatField()),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='timbrado',
            fields=[
                ('nro_timbrado', models.IntegerField(primary_key=True, serialize=False)),
                ('fch_vencimiento_timbrado', models.DateField()),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='factura_compra_detalle',
            fields=[
                ('id_factura_compra_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('cant_periferico', models.IntegerField()),
                ('subtotal_periferico', models.FloatField()),
                ('id_factura_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.factura_compra')),
                ('id_periferico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.perifericos')),
            ],
        ),
        migrations.AddField(
            model_name='factura_compra',
            name='nro_timbrado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.timbrado'),
        ),
    ]
