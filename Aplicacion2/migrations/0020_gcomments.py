# Generated by Django 4.0.5 on 2022-09-02 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Aplicacion2', '0019_gpost_video_alter_grupo_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='GComments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gcomments', to='Aplicacion2.gpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]