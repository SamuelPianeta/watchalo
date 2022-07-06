from .views import creacionPost, detallePost, editarPost, eliminarPost, Inicio, login_request, registro
from django.contrib.auth.views import LogoutView

from django.urls import path


app_name = 'Aplicacion1'
urlpatterns = [
    path('Inicio/', Inicio.as_view(), name='Inicio'),
    path('PostCrear/', creacionPost, name='PostCrear'),
    #path('leerPost/', leerPost, name='leerPost'),
    path('detallePost/<pk>', detallePost.as_view(), name='detallePost'),
    path('editarPost/<pk>', editarPost.as_view(), name='editarPost'),
    path('post_confirm_delete/<pk>', eliminarPost.as_view(), name='post_confirm_delete'),
    path('login/', login_request, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', LogoutView.as_view(template_name='Aplicacion1/logout.html'), name='logout'),
    ]