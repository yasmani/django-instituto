from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    messages.success(request,'Lista de Cursos')
    return render(request, "gestioncursos.html",{"cursos": cursos})

def registrarcurso(request):
    codigo = request.POST['textcodigo']
    nombre = request.POST['textnombre']
    creditos = request.POST['numcredito']

    curso = Curso.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    messages.success(request,'Curso Registrado..')
    return redirect('/')



def editarcurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicioncurso.html",{"curso": curso})


def editacurso(request):
    codigo = request.POST['textcodigo']
    nombre = request.POST['textnombre']
    creditos = request.POST['numcredito']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre=nombre
    curso.creditos=creditos
    curso.save()
    messages.success(request,'Curso Editado..')
    return redirect('/')


def eliminarcurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request,'Curso Eliminado..')
    return redirect('/')

