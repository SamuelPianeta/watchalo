# Generated by Django 4.0.5 on 2022-07-19 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion2', '0005_alter_usuario2_usuario_gpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpost',
            name='related',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion2.grupo'),
        ),
    ]
