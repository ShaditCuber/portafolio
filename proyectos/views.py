from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def inicio(request):
    proyectos = Proyecto.objects.all()

    return render(request, 'inicio.html', {'proyectos': proyectos})