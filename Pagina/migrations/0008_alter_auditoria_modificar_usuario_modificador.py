# Generated by Django 3.2.6 on 2022-02-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0007_auditoria_modificar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditoria_modificar',
            name='usuario_modificador',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
