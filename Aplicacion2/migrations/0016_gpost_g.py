# Generated by Django 4.0.5 on 2022-08-15 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion2', '0015_alter_grupo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpost',
            name='g',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion2.grupo'),
        ),
    ]
