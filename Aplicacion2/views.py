
from django.shortcuts import render, redirect, get_object_or_404


from .models import *
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from Aplicacion2.forms import PostForm, GrupoCreateForm, GrupoCommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.


class listaGrupos(ListView):
    model = Grupo
    template_name = 'Aplicacion2/grupo_grupo_list.html'
    
def grupoView(request, gru):
    grupo_posts = GPost.objects.filter( grupo = gru).order_by('-fechaPublicacion')
    return render(request, 'Aplicacion2/grupo.html', {'grupo': gru, 'grupo_posts': grupo_posts})


def creacionPost(request, gru):
    grupo_posts = GPost.objects.filter( grupo = gru)
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.grupo = gru
            post.user = current_user
            post.save()
            return redirect('Aplicacion2:grupo', gru=gru)
            
    else:
        form = PostForm()
    return render(request, 'Aplicacion2/post_grupo_form.html', {'form': form,'grupo': gru, 'grupo_posts': grupo_posts })

class DetailPostView(DetailView):
    model = GPost
    template_name = 'Aplicacion2/detail_post.html'

class UpdatePostView(UpdateView):
    model = GPost
    form_class = PostForm
    template_name = 'Aplicacion2/edit_post.html'


class DeletePostView(DeleteView):
    model = GPost
    template_name = 'Aplicacion2/delete_post.html'
    success_url = reverse_lazy('Aplicacion2:grupos')

#class AddGrupoView(CreateView):
    #model = Grupo
    #template_name = 'Aplicacion2/add_grupo.html'
    #fields = '__all__'

def creacionGrupo(request):
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = GrupoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            grupo =form.save(commit=False)
            grupo.creator = current_user
            grupo.save()
            return redirect('Aplicacion2:grupos')
    else:
        form = GrupoCreateForm()
    return render(request, 'Aplicacion2/add_grupo.html', {'form': form})

class UpdateGrupoView(UpdateView):
    model = Grupo
    form_class = GrupoCreateForm
    template_name = 'Aplicacion2/editarGrupo.html'

class DeleteGrupoView(DeleteView):
    model = Grupo
    template_name = 'Aplicacion2/deleteGrupo.html'
    success_url = reverse_lazy('Aplicacion2:grupos')

# grupo comentarios ---------------------------------------------------------------------------

class AgregarGrupoComentario(CreateView):
    model = GComments
    form_class = GrupoCommentForm
    template_name = 'Aplicacion2/add_g_comentario.html'
    

    def form_valid(self, form):
        form.instance.gpost_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        form.instance.user_id = self.request.user.id
       
        return super().form_valid(form)
    
    success_url = '/Aplicacion2/grupos/'

class EditarGrupoComentario(UpdateView):
    model = GComments
    success_url = '/Aplicacion2/grupos/'
    fields = ['body']

class EliminarGrupoComentario(DeleteView):
    model = GComments
    template_name ='Aplicacion2/deleteComentarioGrupo.html'
    success_url = reverse_lazy('Aplicacion2:grupos')