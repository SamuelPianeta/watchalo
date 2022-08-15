
from django.shortcuts import render, redirect, get_object_or_404


from .models import *
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from Aplicacion2.forms import PostForm, GrupoCreateForm
# Create your views here.


class listaGrupos(ListView):
    model = Grupo
    template_name = 'Aplicacion2/grupo_grupo_list.html'
    
def grupoView(request, gru):
    grupo_posts = GPost.objects.filter( grupo = gru).order_by('-fechaPublicacion')
    return render(request, 'Aplicacion2/grupo.html', {'grupo': gru, 'grupo_posts': grupo_posts})

def creacionPost(request):
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('Aplicacion2:grupos')
    else:
        form = PostForm()
    return render(request, 'Aplicacion2/post_grupo_form.html', {'form': form})

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

class AddGrupoView(CreateView):
    model = Grupo
    template_name = 'Aplicacion2/add_grupo.html'
    fields = '__all__'

