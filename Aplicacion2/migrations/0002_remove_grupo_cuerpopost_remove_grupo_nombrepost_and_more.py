# Generated by Django 4.0.5 on 2022-07-18 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='CuerpoPost',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='nombrePost',
        ),
        migrations.CreateModel(
            name='PostGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePost', models.CharField(max_length=255)),
                ('CuerpoPost', models.TextField(max_length=5000)),
                ('grupoAsociado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacion2.grupo')),
            ],
        ),
    ]
