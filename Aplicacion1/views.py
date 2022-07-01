from dataclasses import fields
from webbrowser import get
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from Aplicacion1.models import Post
from Aplicacion1.forms import PostForm, UserRegistrationForm
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class Inicio(LoginRequiredMixin,ListView):
    model = Post
    queryset = Post.objects.all().order_by('-fechaPublicacion')
    template_name = 'Aplicacion1/Inicio.html'

class creacionPost(CreateView):
    model = Post
    form_class = PostForm
    #fields ='__all__'
    success_url = '/Aplicacion1/Inicio/'

#def leerPost(request):
    #post = Post.objects.all().order_by('-fechaPublicacion')
    #contexto = {'post': post}
    #return render(request, 'Aplicacion1/leerPost.html', contexto)

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
