from django.contrib import admin

# Register your models here.
from Aplicacion1.models import *

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Perfil)

