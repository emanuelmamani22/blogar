from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Post
from .forms import EntradaForm, RegistrarUser

# Create your views here.

def index(request):
   hola='hola'
   return render(request, 'index.html', {'hola':hola})


def entrada(request):
   if request.method == 'POST':
     form=EntradaForm(request.POST)
     if form.is_valid():
       titulo_b=request.POST['titulo']
       texto_b=request.POST['texto']
       usuario=request.user
       entrada_b=Post(titulo=titulo_b, contenido=texto_b, autor=asuario)
       entrada_b.save()
       return HttpResponseRedirect('/')
     else :
         return render(request, 'entrada.html', {'form':form})
   else :
       form = EntradaForm()
   return render(request, 'entrada.html', {'form':form})


def registrar(request):
   if request.method == 'POST':
     form=RegistrarUser(request.POST)
     if form.is_valid():
        user_f=request.POST['username']
        name_f=request.POST['nombre']
        namelast_f=request.POST['apellido']
        email_f=request.POST['email']
        password_f=request.POST['password']
        
        insert=User.objects.create_user(username=user_f, first_name=name_f, last_name=namelast_f, email=email_f, password=password_f)
        insert.save()
        
        return HttpResponseRedirect('/')
     else :
        return render(request, 'registro.html', {'form':form})
   else :
        form=RegistrarUser()
   return render(request, 'registro.html', {'form':form})
