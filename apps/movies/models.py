from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class BaseName(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Categories(BaseName):
    minimum_age = models.IntegerField(verbose_name='Edad Minima')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Especialidades'


class Movies(BaseName):
    description = models.CharField(max_length=256, verbose_name='Teléfono')
    image = models.ImageField(upload_to='movies', verbose_name='Imagen Carnet')
    release_date = models.DateField(verbose_name='Fecha de atención')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Especialidad')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def get_edit_url(self):
        return reverse_lazy('movies:movies-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('movies:movies-delete', kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse_lazy('movies:movies-detail', kwargs={'pk': self.pk})
