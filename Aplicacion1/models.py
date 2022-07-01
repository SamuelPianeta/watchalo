from distutils.command.upload import upload
import email
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateTimeField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre +' '+ self.apellido

class Post(models.Model):
    nombrePost = models.CharField(max_length=50)
    CuerpoPost = RichTextField(blank = True, null = True, max_length=5000)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(blank = True, null = True, upload_to="imagenes/")
    def __str__(self) -> str:
        return self.nombrePost + ' / ' + self.CuerpoPost

    