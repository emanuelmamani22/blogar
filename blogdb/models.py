from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Categoria(models.Model):
     nombre = models.CharField(max_length=50, unique=True)
     is_active = models.BooleanField(default=True)
     
     def __unicode__(self):
        return self.nombre

class Post(models.Model):
     titulo = models.CharField(max_length=200)
     slug = models.SlugField(max_length=200)
     contenido = models.TextField()
     publico = models.BooleanField(default=True)
     autor = models.ForeignKey(User)
     creado = models.DateTimeField(auto_now_add=True)
     
     def __unicode__(self):
        return self.titulo
     
     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not getattr(self, 'slug'):
              self.slug = slugify(self.titulo)
              super(Post, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields) 
     
     
