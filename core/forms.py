from django import forms
from .models import Area, Publico, Curso
from django.contrib.auth.forms import UserCreationForm

class UsuarioCadastroForm(UserCreationForm):
    class Meta:
        model = UsuarioCadastroForm
        fealds = [
            'cpf',
            'nascimento',
            'username',
            'email',
            'frst_name',
            'last_ame',
            'password1',
            'password2'       
        ]

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']