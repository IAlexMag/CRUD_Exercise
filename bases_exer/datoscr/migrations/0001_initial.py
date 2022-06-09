# Generated by Django 4.0.5 on 2022-06-09 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen')),
            ],
        ),
    ]
