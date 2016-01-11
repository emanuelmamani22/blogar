from django.shortcuts import render

# Create your views here.

def index(request):
   hola='hola'
   return render(request, 'index.html', {'hola':hola})
