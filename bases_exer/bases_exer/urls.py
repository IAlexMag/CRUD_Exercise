"""bases_exer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from datoscr import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('books/', views.books, name='books'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit'),
    path('formulario/', views.formulario, name='formulario'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('edit/<int:id>', views.edit, name='edit')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
