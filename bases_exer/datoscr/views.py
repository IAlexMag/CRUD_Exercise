from django.shortcuts import render, redirect
from .models import Libro
from django.http import HttpResponse
from .forms import LibroForm

# Create your views here.
def index (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'navigation/about.html')

def books (request):
    Libros = Libro.objects.all()
    return render(request, 'navigation/books.html', {'Libros': Libros})

def create (request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('books')
    return render(request, 'navigation/create.html', {'formulario': formulario})

def edit (request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('books')
    return render(request, 'navigation/edit.html', {'formulario': formulario})

def formulario (request):
    return render(request, 'formulario.html')

def eliminar (request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('books')