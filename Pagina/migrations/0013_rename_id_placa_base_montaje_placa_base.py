# Generated by Django 3.2.6 on 2022-02-08 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0012_rename_placa_base_montaje_id_placa_base'),
    ]

    operations = [
        migrations.RenameField(
            model_name='montaje',
            old_name='id_placa_base',
            new_name='placa_base',
        ),
    ]