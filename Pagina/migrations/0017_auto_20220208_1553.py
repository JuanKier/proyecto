# Generated by Django 3.2.6 on 2022-02-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0016_rename_placa_base_montaje_id_placa_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='montaje',
            name='tipo_almacenamiento',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='montaje',
            name='tipo_fuente',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='montaje',
            name='tipo_placa_video',
            field=models.IntegerField(null=True),
        ),
    ]
