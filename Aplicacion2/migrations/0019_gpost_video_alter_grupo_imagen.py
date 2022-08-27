# Generated by Django 4.0.5 on 2022-08-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion2', '0018_grupo_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpost',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='Subir video'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='imagen',
            field=models.ImageField(blank=True, default='grupos_default_img', null=True, upload_to='images/', verbose_name='Subir imagen'),
        ),
    ]
