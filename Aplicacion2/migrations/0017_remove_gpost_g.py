# Generated by Django 4.0.5 on 2022-08-16 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion2', '0016_gpost_g'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpost',
            name='g',
        ),
    ]