from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, blank=True,null=True,on_delete=models.CASCADE) 
    perfilImagen = models.ImageField(default='default_perfil.jpg')
    def __str__(self) -> str:
        return f"Perfil de {self.user.username}"
    def following(self):
        users_ids = Relationship.objects.filter(from_user=self.user)\
                                 .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=users_ids)

    def followers(self):
        users_ids = Relationship.objects.filter(to_user=self.user)\
                                 .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=users_ids)
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateTimeField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre +' '+ self.apellido

class Post(models.Model):
    nombrePost = models.CharField(max_length=50, verbose_name = 'Titulo')
    CuerpoPost = RichTextField(blank = True, null = True, max_length=5000, verbose_name = 'Contenido')
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE, related_name = "posts")
    imagen = models.ImageField(blank = True, null = True, upload_to="images/", verbose_name="Subir imagen")
    video = models.FileField(blank = True, null = True, upload_to="videos/", verbose_name="Subir video")
    likes = models.ManyToManyField(User, related_name="likes", blank = True, null = True)
    dislikes = models.ManyToManyField(User, related_name="dislikes", blank = True, null = True)

    
    
        
    def __str__(self) -> str:
        return f"{self.user.username}: {self.CuerpoPost}" 

class comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.nombrePost, self.name)    

class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name="relationships", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="related_to", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_user} to {self.to_user}"
    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user',]),
        ]