# Generated by Django 4.0.5 on 2022-07-18 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0018_relationship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
