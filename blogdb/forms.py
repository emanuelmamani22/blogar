from django import forms
from .models import Post
from django.contrib.auth.models import User


class EntradaForm(forms.Form):
     titulo_blog = forms.CharField(max_length=200)
     texto = forms.CharField(widget=forms.Textarea)
     
     def clean_titulo_blog(self):
        """Comprueva que no exista otra entrada con el mismo nombre"""
        titulo_blog = self.cleaned_data['titulo_blog']
        if Post.objects.filter(titulo=titulo_blog):
          raise forms.ValidationError('Nombre repetido')
        return titulo_blog


class RegistrarUser(forms.Form):
     username=forms.CharField(min_length=5)
     nombre=forms.CharField(min_length=5)
     apellido=forms.CharField(min_length=5)
     email=forms.EmailField()
     password= forms.CharField(min_length=5, widget=forms.PasswordInput())
     password2= forms.CharField(widget=forms.PasswordInput())
     
     def clean_username(self):
        username=self.cleaned_data['username']
        if User.objects.filter(username=username):
           raise forms.ValidationError('El nombre de usario ya existe')
        return username

     def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email):
           raise forms.ValidationError('Ese email ya esta asociado a una cuenta')
        return email

     def clean_password2(self):
        password=self.cleaned_data['password']
        password2=self.cleaned_data['password2']
        if password != password2:
           raise forms.ValidationError('El password no coincide')
        return password2


class LoginForm(forms.Form):
     username = forms.CharField(min_length=5)
     password = forms.CharField(min_length=5, widget=forms.PasswordInput())

class Comentar(forms.Form):
     comentario = forms.CharField(widget=forms.Textarea)
