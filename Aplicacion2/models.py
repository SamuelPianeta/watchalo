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
    imagen = models.ImageField(blank = True, null = True, upload_to="images/", verbose_name="Subir imagen", default ="grupos_default_img")

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
    video = models.FileField(blank = True, null = True, upload_to="videos/", verbose_name="Subir video")

    grupo = models.CharField(max_length=255, default='Random')
    
    def __str__(self) -> str:
        return self.user.username +"/" + self.CuerpoPost

    def get_absolute_url(self):
        return reverse('Aplicacion2:grupos')

class GComments(models.Model):
    id = models.AutoField(primary_key=True)
    gpost = models.ForeignKey(GPost, related_name = "Gcomments", on_delete= models.CASCADE)
    user = models.ForeignKey(User, related_name="usuario2", on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' % (self.gpost.nombrePost, self.name, self.name) 
    

     





    
    