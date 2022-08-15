from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to="proyectos/imagenes/")
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
