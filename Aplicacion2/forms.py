from django import forms
from .models import GPost, Grupo

choices = Grupo.objects.all().values_list('nombre', 'nombre')
choice_list= []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = GPost
        fields = ['nombrePost', 'CuerpoPost', 'imagen'] 

        widgets = {
            #'grupo': forms.Select(choices = choice_list, attrs={ 'class': 'form-control' }),
            'nombrePost': forms.TextInput(attrs={ 'class': 'form-control' }),
            'CuerpoPost': forms.Textarea(attrs={ 'class': 'form-control' }),

        }

class GrupoCreateForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre','detalles', 'imagen']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'detalles': forms.Textarea(attrs={'class': 'form-control'}),
        }