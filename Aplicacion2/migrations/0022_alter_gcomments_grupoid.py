# Generated by Django 4.0.5 on 2022-09-06 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion2', '0021_gcomments_grupoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcomments',
            name='grupoID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo_id', to='Aplicacion2.grupo'),
        ),
    ]
