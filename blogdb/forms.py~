from django import forms
from .models import Post



class EntradaForm(forms.Form):
     titulo_blog = forms.Charfield(max_length=200)
     texto = forms.TextField()
     
     def clean_titulo_blog(self):
        """Comprueva que no exista otra entrada con el mismo nombre"""
        titulo_blog = self.cleaned_data['titulo_blog']
        if Post.objects.filter(titulo=titulo_blog):
          raise forms.ValidationError('Nombre repetido')
        return titulo_blog
