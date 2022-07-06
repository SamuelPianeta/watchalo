from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, blank=True,null=True,on_delete=models.CASCADE) 
    def __str__(self) -> str:
        return f"Perfil de {self.user.username}"

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
    user = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE, related_name = "posts")
    imagen = models.ImageField(blank = True, null = True, upload_to="images/", verbose_name="Subir imagen")
    def __str__(self) -> str:
        return f"{self.user.username}: {self.CuerpoPost}" 

    