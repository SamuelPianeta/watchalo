
from django.urls import path, re_path
from .views import *
from django.contrib.auth.decorators import login_required


app_name = 'Aplicacion2'
urlpatterns = [
    path('grupos/', listaGrupos.as_view(), name='grupos'),
    path('grupos/<str:gru>/', login_required(grupoView), name='grupo'),
    path('grupos/<str:gru>/post/', login_required(creacionPost), name='post'),
    #path('post/<int:pk>', DetailPostView.as_view(), name = 'detail_post'),
    path('post/edit/<int:pk>', login_required(UpdatePostView.as_view()), name = 'edit_post'),
    path('post/delete/<int:pk>', login_required(DeletePostView.as_view()), name = 'delete_post'),
    path('grupos/add/new/', login_required(creacionGrupo), name = 'add_grupo'),
    path('grupos/edit/<int:pk>', login_required(UpdateGrupoView.as_view()), name = 'edit_grupo'),
    path('grupos/delete/<int:pk>', login_required(DeleteGrupoView.as_view()), name = 'delete_grupo'),
    path('grupos/comment/<int:pk>', login_required(AgregarGrupoComentario.as_view()), name = 'add_g_comment'),
    ]