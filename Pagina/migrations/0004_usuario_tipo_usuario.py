# Generated by Django 3.2.7 on 2021-11-24 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0003_alter_usuario_nombre_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.IntegerField(null=True),
        ),
    ]
