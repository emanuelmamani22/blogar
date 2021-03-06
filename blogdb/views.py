from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Post, Comentario
from .forms import EntradaForm, RegistrarUser, LoginForm, Comentar
from django.contrib.auth import authenticate, login, logout
from .funciones import generar_codigo

# Create your views here.

def index(request):
   hola='hola'
   return render(request, 'index.html', {'hola':hola})


def entrada(request):
   if request.user.is_authenticated():
     if request.method == 'POST':
       form=EntradaForm(request.POST)
       if form.is_valid():
         titulo_b=request.POST['titulo_blog']
         texto_b=request.POST['texto']
         usuario=request.user
         codigo = generar_codigo()
         entrada_b=Post(titulo=titulo_b, contenido=texto_b, autor=usuario, codigo_e=codigo)
         entrada_b.save()
         return HttpResponseRedirect('/')
       else :
           return render(request, 'entrada.html', {'form':form})
     else :
         form = EntradaForm()
   else :
     return HttpResponseRedirect('/login')
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

def login_views(request):
   mensaje=None
   if request.method == 'POST':
     form = LoginForm(request.POST)
     if form.is_valid():
       user_f = request.POST['username']
       password_f = request.POST['password']
       user = authenticate(username=user_f, password=password_f)
       if user is not None:
          if user.is_active:
             login(request, user)
             return HttpResponseRedirect('/')
          else :
             mensaje = "Tu usuario no esta activo"
       else :
          mensaje = "Nombre de usuario y/o password incorrectos"
     else :
       return render(request, 'login.html', {'mensaje':mensaje, 'form':form})
   else :
     form = LoginForm()
   return render(request, 'login.html', {'mensaje':mensaje, 'form':form})

def logout_views(request):
    logout(request) 
    # Redireccciona a una pagina de entrada correcta.    
    return HttpResponseRedirect('/')

def verblog(request, codigo, slug):
   e = Post.objects.get(codigo_e=codigo, slug=slug)
   cc = e.id
   try :
       c = Comentario.objects.filter(codigo_p=cc)
   except :
       c=None
   if request.method == 'POST':
      form=Comentar(request.POST)
      if form.is_valid():
        comentario_f = request.POST['comentario']
        insertar = Comentario(contenido_c=comentario_f, codigo_p=e)
        insertar.save()
        return HttpResponseRedirect('/verblog/'+codigo+'/'+slug)
   else :
      form=Comentar()
   return render(request, 'verblog.html', {'e':e, 'c':c,'form':form})
