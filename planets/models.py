from django.db import models

# Create your models here.
class Universe(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    class Meta:
        verbose_name = 'Universo'
        verbose_name_plural = 'Universos'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    universe = models.ForeignKey(Universe, on_delete= models.CASCADE, related_name= 'get_planets', verbose_name='Universo')
    description = models.TextField(verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')

    class Meta:
        verbose_name = 'Planeta'
        verbose_name_plural = 'Planetas'
        ordering = ['name']
    
    def __str__(self):
        return self.name
