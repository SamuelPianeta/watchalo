# Generated by Django 4.0.5 on 2022-07-25 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion2', '0010_gpost_grupo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gpost',
            old_name='grupo',
            new_name='grupoG',
        ),
    ]
