from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(datetime.date.today)
    imagen = models.ImageField(upload_to="blog/post/imagenes/", blank=True)

    def __str__(self):
        return self.titulo
