from .views import creacionPost, detallePost, editarPost, eliminarPost, Inicio, login_request, registro, perfil, error404, follow, unfollow, agregarComentario
from django.contrib.auth.views import LogoutView

from django.urls import path
from django.conf.urls import handler400

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
    path('perfil/<str:username>/', perfil, name='perfil'),
    path('follow/<str:username>/', follow, name='follow'),
    path('unfollow/<str:username>/', unfollow, name='unfollow'),
    #path('like/<int:pk>',addLike.as_view(), name='like'),
   # path('dislike/<int:pk>/',addDislike.as_view(), name='dislike')
    path('coment/<int:pk>', agregarComentario.as_view(), name='add_comentario'),
    ]

handler400 = error404.as_view()