from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=255, verbose_name='nombre')
    price = models.DecimalField(max_digits=10   , decimal_places=2, verbose_name='precio')  
    description = models.TextField(max_length=300, verbose_name='descripción')
    available = models.BooleanField(default=True, verbose_name='disponible')
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name='foto')


    def __str__(self):
        return self.name
