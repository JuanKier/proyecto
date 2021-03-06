# Generated by Django 3.2.8 on 2022-02-21 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigo_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('ruc_cliente', models.CharField(max_length=50)),
                ('telefono_cliente', models.CharField(max_length=30)),
                ('direccion_cliente', models.CharField(max_length=200)),
                ('genero_cliente', models.IntegerField(null=True)),
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
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('codigo_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='factura_compra',
            fields=[
                ('id_factura_compra', models.AutoField(primary_key=True, serialize=False)),
                ('nro_factura_compra', models.IntegerField()),
                ('fch_factura_compra', models.DateField()),
                ('condicion_factura_compra', models.IntegerField()),
                ('iva10_factura_compra', models.FloatField()),
                ('total_factura_compra', models.FloatField()),
            ],
        ),
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
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('codigo_nacionalidad', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_nacionalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('codigo_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=50)),
                ('razon_social_proveedor', models.CharField(max_length=50)),
                ('ruc_proveedor', models.CharField(max_length=50)),
                ('telefono_proveedor', models.CharField(max_length=30)),
                ('direccion_proveedor', models.CharField(max_length=200)),
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
            name='Tipo_Cpu',
            fields=[
                ('id_tipo_cpu', models.AutoField(primary_key=True, serialize=False)),
                ('desc_tipo_cpu', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Gabinete',
            fields=[
                ('id_tipo_gabinete', models.AutoField(primary_key=True, serialize=False)),
                ('desc_tipo_gabinete', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Ram',
            fields=[
                ('id_tipo_ram', models.AutoField(primary_key=True, serialize=False)),
                ('desc_tipo_ram', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=10, unique=True)),
                ('password_usuario', models.CharField(max_length=10)),
                ('nombre_completo_usuario', models.CharField(max_length=200)),
                ('tipo_usuario', models.IntegerField(null=True)),
                ('ci_usuario', models.CharField(max_length=20)),
                ('telefono_usuario', models.CharField(max_length=30)),
                ('direccion_usuario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='timbrado',
            fields=[
                ('nro_timbrado', models.IntegerField(primary_key=True, serialize=False)),
                ('fch_vencimiento_timbrado', models.DateField()),
                ('codigo_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
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
            name='Repuestos',
            fields=[
                ('id_repuesto', models.AutoField(primary_key=True, serialize=False)),
                ('cod_repuesto', models.IntegerField(null=True)),
                ('tipo_repuesto', models.IntegerField(null=True)),
                ('marca_repuesto', models.CharField(max_length=30)),
                ('descripcion_repuesto', models.CharField(max_length=200)),
                ('precio_compra_repuesto', models.IntegerField()),
                ('precio_venta_repuesto', models.IntegerField()),
                ('stock_repuesto', models.IntegerField(default=0)),
                ('imagen_repuesto', models.ImageField(null=True, upload_to='repuestos')),
                ('nombre_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('codigo_rep', models.AutoField(primary_key=True, serialize=False)),
                ('equipo_rep', models.IntegerField(null=True)),
                ('desc_equipo_rep', models.CharField(max_length=200)),
                ('horas_rep', models.IntegerField(null=True)),
                ('actividades_rep', models.CharField(max_length=200)),
                ('inicio_rep', models.DateField()),
                ('fin_rep', models.DateField()),
                ('estado_rep', models.IntegerField(default=1, null=True)),
                ('nombre_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.cliente')),
                ('nombre_completo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.usuario')),
            ],
        ),
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
        migrations.CreateModel(
            name='Placa_base',
            fields=[
                ('id_placa_base', models.AutoField(primary_key=True, serialize=False)),
                ('cod_placa_base', models.IntegerField(null=True)),
                ('marca_placa_base', models.CharField(max_length=30)),
                ('descripcion_placa_base', models.CharField(max_length=200)),
                ('precio_compra_placa_base', models.IntegerField()),
                ('precio_venta_placa_base', models.IntegerField()),
                ('stock_placa_base', models.IntegerField(default=0)),
                ('imagen_placa_base', models.ImageField(null=True, upload_to='placa_base')),
                ('nombre_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
                ('tipo_cpu_placa_base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.tipo_cpu')),
                ('tipo_gabinete_placa_base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.tipo_gabinete')),
                ('tipo_ram_placa_base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.tipo_ram')),
            ],
        ),
        migrations.CreateModel(
            name='Perifericos',
            fields=[
                ('id_periferico', models.AutoField(primary_key=True, serialize=False)),
                ('cod_periferico', models.IntegerField(null=True)),
                ('tipo_periferico', models.IntegerField(null=True)),
                ('marca_periferico', models.CharField(max_length=30)),
                ('descripcion_periferico', models.CharField(max_length=200)),
                ('precio_compra_periferico', models.IntegerField()),
                ('precio_venta_periferico', models.IntegerField()),
                ('stock_periferico', models.IntegerField(default=0)),
                ('imagen_periferico', models.ImageField(null=True, upload_to='perifericos')),
                ('nombre_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Montaje',
            fields=[
                ('codigo_montaje', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_placa_video', models.IntegerField(null=True)),
                ('tipo_fuente', models.IntegerField(null=True)),
                ('tipo_almacenamiento', models.IntegerField(null=True)),
                ('horas_mont', models.IntegerField(null=True)),
                ('actividades_mont', models.CharField(max_length=200)),
                ('inicio_mont', models.DateField()),
                ('fin_mont', models.DateField()),
                ('estado_mont', models.IntegerField(default=1, null=True)),
                ('id_periferico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.perifericos')),
                ('id_placa_base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.placa_base')),
                ('nombre_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.cliente')),
                ('nombre_completo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.usuario')),
                ('tipo_cpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.cpu')),
                ('tipo_gabinete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.gabinete')),
                ('tipo_ram', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.ram')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('codigo_mant', models.AutoField(primary_key=True, serialize=False)),
                ('equipo_mant', models.IntegerField(null=True)),
                ('desc_equipo_mant', models.CharField(max_length=200)),
                ('horas_mant', models.IntegerField(null=True)),
                ('actividades_mant', models.CharField(max_length=200)),
                ('inicio_mant', models.DateField()),
                ('fin_mant', models.DateField()),
                ('estado_mant', models.IntegerField(default=1, null=True)),
                ('nombre_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.cliente')),
                ('nombre_completo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='gabinete',
            name='nombre_proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor'),
        ),
        migrations.AddField(
            model_name='gabinete',
            name='tipo_gabinete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.tipo_gabinete'),
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
            name='codigo_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor'),
        ),
        migrations.AddField(
            model_name='factura_compra',
            name='nro_timbrado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina.timbrado'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='nombre_proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.proveedor'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='tipo_cpu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.tipo_cpu'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='descripcion_nacionalidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.nacionalidad'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.ciudad'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.departamento'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='nombre_departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.departamento'),
        ),
    ]
