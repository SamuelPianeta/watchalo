# Generated by Django 4.0.5 on 2022-06-29 23:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0005_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='CuerpoPost',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True),
        ),
    ]