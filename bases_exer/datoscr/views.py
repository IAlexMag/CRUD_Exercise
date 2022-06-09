from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'navigation/about.html')

def books (request):
    return render(request, 'navigation/books.html')

def create (request):
    return render(request, 'navigation/create.html')

def edit (request):
    return render(request, 'navigation/edit.html')

def formulario (request):
    return render(request, 'formulario.html')
