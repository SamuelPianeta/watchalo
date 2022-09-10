


from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from Aplicacion1.models import Post, Relationship, comments, Perfil
from Aplicacion1.forms import PostForm, UserRegistrationForm,CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Muro principal / CRUD de posts------------------------------------------------------------------------

class Inicio(LoginRequiredMixin,ListView):
    model = Post
    queryset = Post.objects.all().order_by('-fechaPublicacion')
    template_name = 'Aplicacion1/Inicio.html'

def creacionPost(request):
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('Aplicacion1:Inicio')
    else:
        form = PostForm()
    return render(request, 'Aplicacion1/post_form.html', {'form': form})

class  detallePost(DetailView):
    model = Post
    template_name = 'Aplicacion1/detallePost.html'

class editarPost(UpdateView):
    model = Post
    success_url ='/Aplicacion1/Inicio/'
    fields = ['nombrePost','CuerpoPost']

class eliminarPost(DeleteView):
    model = Post
    success_url = '/Aplicacion1/Inicio/'

class error404(TemplateView):
    template_name = 'Aplicacion1/error_404.html'


# Perfil y follows(viendo/viendote)---------------------------------------------------------------------

def perfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render (request, 'Aplicacion1/perfil.html', {'posts': posts, 'user': user})

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user =to_user_id)
    rel.save()
    mensaje = f"Siguiendo a {username}" 
    return render(request, 'Aplicacion1/Inicio.html', {'mensaje': mensaje})

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship.objects.filter(from_user=current_user.id, to_user_id=to_user_id).get()
    rel.delete()
    mensaje = f"Ya no sigues a {username}" 
    return render(request, 'Aplicacion1/Inicio.html', {'mensaje': mensaje})

# Comentarios ------------------------------------------------------------------------------------------

class agregarComentario(CreateView):
    model = comments
    form_class = CommentForm
    template_name = 'Aplicacion1/add_comentario.html'


    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    success_url = '/Aplicacion1/Inicio/'


class editarComentario(UpdateView):
    model = comments 
    success_url ='/Aplicacion1/Inicio/'
    fields = ['body']

class eliminarComentario(DeleteView):
    model = comments
    success_url = '/Aplicacion1/Inicio/'


# Login y registro --------------------------------------------------------------------------------------

def login_request(request):
    if request.method == 'POST':

            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')

                user = authenticate(username=usuario, password=contra)

                if user is not None:
                    login(request, user)
                    return render(request, 'Aplicacion1/Inicio.html', {'mensaje': f'Bienvenido {usuario}'})
                else:
                    return render(request, 'Aplicacion1/Inicio.html', {'error': 'Datos incorrectos'})
            else:
                return render(request, 'Aplicacion1/Inicio.html', {'errorForm': 'Formulario Invalido'})
    form = AuthenticationForm

    return render(request, "Aplicacion1/login.html", {"form": form})
            
def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'Aplicacion1/Inicio.html',{'mensaje':'Usuario creado'})
    
    else:
        form = UserRegistrationForm

    return render(request, 'Aplicacion1/registro.html', {'form': form})

class ActualizarPerfil(UpdateView):
    model = Perfil
    success_url = '/Aplicacion1/Inicio/'
    fields = '__all__'

