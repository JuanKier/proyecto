# Generated by Django 3.2.6 on 2022-02-08 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0009_rename_tipo_periferico_montaje_id_periferico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='montaje',
            old_name='placa_base',
            new_name='id_placa_base',
        ),
    ]