# Generated by Django 4.0.5 on 2022-07-18 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0018_relationship_and_more'),
        ('Aplicacion2', '0002_remove_grupo_cuerpopost_remove_grupo_nombrepost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario_grupo',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='usuario_grupo',
            name='usuario_en_grupo',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='nombreGrupo',
        ),
        migrations.RemoveField(
            model_name='usuario2',
            name='usuario2',
        ),
        migrations.AddField(
            model_name='grupo',
            name='detalles',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario2',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion1.usuario'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='PostGrupo',
        ),
        migrations.DeleteModel(
            name='Usuario_Grupo',
        ),
        migrations.AddField(
            model_name='grupo_usuario',
            name='grupo_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion2.grupo'),
        ),
        migrations.AddField(
            model_name='grupo_usuario',
            name='usuario_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion2.usuario2'),
        ),
    ]
