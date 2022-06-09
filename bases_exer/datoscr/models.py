from django.db import models

# Create your models here.
class Libro (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Imagen', null=True)
    autor = models.CharField(max_length=50, verbose_name='Autor', null=True)
    editorial = models.CharField(max_length=50, verbose_name='Editorial', null=True)
    año = models.DateField(max_length=25, verbose_name='Año', null=True)

    def __str__(self):
        fila = "Titulo:" + self.titulo + " - " + "Autor:" + self.autor
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()