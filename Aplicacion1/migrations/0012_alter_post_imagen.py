# Generated by Django 4.0.5 on 2022-07-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0011_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Subir imagen'),
        ),
    ]
