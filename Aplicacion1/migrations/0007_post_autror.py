# Generated by Django 4.0.5 on 2022-07-05 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0006_alter_post_cuerpopost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='autror',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion1.usuario'),
        ),
    ]
