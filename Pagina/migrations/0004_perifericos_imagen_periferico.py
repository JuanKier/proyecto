# Generated by Django 3.2.6 on 2022-02-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0003_alter_perifericos_tipo_periferico'),
    ]

    operations = [
        migrations.AddField(
            model_name='perifericos',
            name='imagen_periferico',
            field=models.ImageField(null=True, upload_to='perifericos'),
        ),
    ]