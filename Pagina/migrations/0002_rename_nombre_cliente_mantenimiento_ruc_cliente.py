# Generated by Django 3.2.8 on 2022-02-01 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mantenimiento',
            old_name='nombre_cliente',
            new_name='ruc_cliente',
        ),
    ]
