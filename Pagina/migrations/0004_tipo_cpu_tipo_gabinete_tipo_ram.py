# Generated by Django 3.2.6 on 2022-02-04 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0003_auto_20220204_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Cpu',
            fields=[
                ('id_tipo_cpu', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cpu', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Gabinete',
            fields=[
                ('id_tipo_gabinete', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_gabinete', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Ram',
            fields=[
                ('id_tipo_ram', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_ram', models.CharField(max_length=20)),
            ],
        ),
    ]
