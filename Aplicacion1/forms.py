
from django import forms
from .models import Post, Usuario, comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('nombrePost', 'CuerpoPost', 'imagen', 'video')

        widgets = {
            'nombrePost': forms.TextInput(attrs={ 'class': 'form-control' }),
            'CuerpoPost': forms.Textarea(attrs={ 'class': 'form-control' })

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'body': forms.Textarea(attrs={ 'class': 'form-control' })
            

        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        help_texts={k:"" for k in fields}