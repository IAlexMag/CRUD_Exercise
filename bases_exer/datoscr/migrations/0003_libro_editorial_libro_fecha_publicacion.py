# Generated by Django 4.0.5 on 2022-06-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datoscr', '0002_libro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.CharField(max_length=50, null=True, verbose_name='Editorial'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(null=True, verbose_name='Fecha de publicación'),
        ),
    ]
