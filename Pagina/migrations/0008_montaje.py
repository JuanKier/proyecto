# Generated by Django 3.2.6 on 2022-02-08 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0007_cpu_gabinete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Montaje',
            fields=[
                ('codigo_montaje', models.AutoField(primary_key=True, serialize=False)),
                ('horas_mont', models.IntegerField(null=True)),
                ('actividades_mont', models.CharField(max_length=200)),
                ('inicio_mont', models.DateField()),
                ('fin_mont', models.DateField()),
                ('estado_mont', models.IntegerField(default=1, null=True)),
                ('nombre_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.cliente')),
                ('nombre_completo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.usuario')),
                ('placa_base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.placa_base')),
                ('tipo_cpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.cpu')),
                ('tipo_gabinete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.gabinete')),
                ('tipo_periferico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.perifericos')),
                ('tipo_ram', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pagina.ram')),
            ],
        ),
    ]
