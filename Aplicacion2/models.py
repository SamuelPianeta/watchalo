from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User,blank = True, null=True, verbose_name="creator", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255,blank=True, null=True,)
    detalles = models.CharField(max_length=255,blank=True, null=True,)
    def __str__(self):
        return self.nombre + " " + str(self.id)
    def get_absolute_url(self):
        return reverse('Aplicacion2:grupos')

class GPost(models.Model):
    id = models.AutoField(primary_key=True)
    nombrePost = models.CharField(max_length=50, verbose_name='Titulo de post')
    CuerpoPost = RichTextField(blank = True, null = True, max_length=5000,verbose_name='Que piensas?')
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE, related_name = "post")
    imagen = models.ImageField(blank = True, null = True, upload_to="images/", verbose_name="Subir imagen")
    grupo = models.CharField(max_length=255, default='Random')
    
    def __str__(self) -> str:
        return self.user.username +"/" + self.CuerpoPost

    def get_absolute_url(self):
        return reverse('Aplicacion2:grupos')





    
    