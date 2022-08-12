
from django.urls import path, re_path
from .views import *


app_name = 'Aplicacion2'
urlpatterns = [
    path('grupos/', listaGrupos.as_view(), name='grupos'),
    path('grupos/<str:gru>/', grupoView, name='grupo'),
    path('post/', creacionPost, name='post'),
    path('post/<int:pk>', DetailPostView.as_view(), name = 'detail_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name = 'edit_post'),
    ]